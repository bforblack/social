import concurrent.futures as futures
from protobufs import postmanagement_pb2_grpc, postmanagement_pb2
from google.protobuf.json_format import MessageToDict
from postmanagementservice.post_service import PostManagementService
import grpc
import json
from grpc import StatusCode
from post_scheduler.scheduler import TaskScheduler
import threading
import schedule

from logs.studio_logger import Logger

logger = Logger("postManagementService")


class PostManagement(postmanagement_pb2_grpc.socialPostManagement):
    def getAllPost(self, request, context):



        #requested_data = MessageToDict(request)
        try:
            requested_data = MessageToDict(request)
            logger.info(f"Request for get_all_posts() user_id: {requested_data['registrationId']}"
                        f" media_source: {requested_data['mediaSource']}"
                        f" page_id: {requested_data['pageId']} received...")
            requested_data = MessageToDict(request)
            data = PostManagementService().get_all_posts(requested_data)
            return postmanagement_pb2.getAllPostResponse(mediaSource=requested_data['mediaSource'],
                                                         registrationId=requested_data['registrationId'],
                                                         pageId=requested_data['pageId'],
                                                         postList=json.dumps(data),
                                                         postResponceId=None)


        except Exception as e:
            error_message = f"Error occurred while getting posts for user_id: {requested_data['registrationId']} " \
                            f" media_source: {requested_data['mediaSource']} " \
                            f" page_id: {requested_data['pageId']} : {str(e)}"
            logger.error(error_message)
            context.set_code(StatusCode.INTERNAL)
            context.set_details("Internal Server Error: " + str(e))
            return postmanagement_pb2.postResponse()

    def createPost(self, request, context):

        try:
            requested_data = MessageToDict(request)


            data = PostManagementService().create_post(requested_data)
            # print(requested_data["mediaSource"])
            return postmanagement_pb2.postResponse(postId=data[requested_data["mediaSource"]]["id"])


        except Exception as e:
            error_message = f"Error occurred while creating post for user_id: {requested_data['registrationId']} " \
                            f" media_source: {requested_data['mediaSource']}: {str(e)}"
            logger.error(error_message)
            context.set_code(grpc.StatusCode.INTERNAL)
            context.set_details(error_message)
            return postmanagement_pb2.postResponse()

    def postSchedule(self, request, context):

        requested_data = MessageToDict(request)

        # print('requested_data', requested_data)
        object_data = json.loads(requested_data['Object'])
        scheduleTime = object_data['schedule_time']

        try:
            logger.info(f"Request for postSchedule() user_id: {requested_data['registrationId']}"
                        f" media_source: {requested_data['mediaSource']} received with the post  {scheduleTime}...")

            task_scheduler = TaskScheduler()

            job_id = task_scheduler.store_job(requested_data, scheduleTime)
            task_scheduler.load_jobs(job_id, scheduleTime, PostManagementService().create_post)

            return postmanagement_pb2.postResponse(postId=str(job_id))

        except Exception as e:

            error_message = f"Error occurred while post scheduling for user_id: {requested_data['registrationId']} " \
                            f" media_source: {requested_data['mediaSource']}: {str(e)}"
            logger.error(error_message)
            context.set_code(grpc.StatusCode.INTERNAL)
            context.set_details(error_message)
            return postmanagement_pb2.postResponse()

    def getPost(self, request, context):


        try:
            requested_data = MessageToDict(request)
            logger.info(f"Request for get_post() user_id: {requested_data['registrationId']}"
                        f" media_source: {requested_data['mediaSource']} received...")


            data = PostManagementService().get_post(requested_data)
            return postmanagement_pb2.getAllPostResponse(mediaSource=requested_data['mediaSource'],
                                                         registrationId=requested_data['registrationId'],
                                                         pageId=requested_data['pageId'],
                                                         postList=json.dumps(data),
                                                         postResponceId=None)

        except Exception as e:
            error_message = f"Error occurred while fetching post for user_id: {requested_data['registrationId']} " \
                            f" media_source: {requested_data['mediaSource']}: {str(e)}"
            logger.error(error_message)
            context.set_code(grpc.StatusCode.INTERNAL)
            context.set_details(error_message)
            return postmanagement_pb2.getAllPostResponse()


def server():
    _server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    postmanagement_pb2_grpc.add_socialPostManagementServicer_to_server(PostManagement(), _server)
    _server.add_insecure_port("0.0.0.0:50053")
    _server.start()
    # task scheduler
    schedule.clear()
    task_scheduler = TaskScheduler()
    thread2 = threading.Thread(target=task_scheduler.fetch_and_schedule_tasks,
                               args=(PostManagementService().create_post,))
    # Start the thread
    thread2.start()
    _server.wait_for_termination()


if __name__ == '__main__':
    print('--------Post management Server Started-----------')
    server()
