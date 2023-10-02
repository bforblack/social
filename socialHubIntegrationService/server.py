import concurrent.futures as futures
import json

import grpc

from protobufs import socialhub_pb2_grpc, socialhub_pb2
from social_connectors import SocialHub
from google.protobuf.json_format import MessageToDict

from logs.studio_logger import Logger
logger = Logger("socialHubIntegrationService")


class SocialHubServer(socialhub_pb2_grpc.socialHubConnectors):

    def getUserData(self, request, context):

        try:
            data = SocialHub(**MessageToDict(request)).getUserData()
            return socialhub_pb2.socialHubResponce(responce=json.dumps(data))

        except Exception as e:
            error_message = f"Error occurred while registering user: {str(e)}"
            logger.error(error_message)
            context.set_code(grpc.StatusCode.INTERNAL)
            context.set_details(error_message)
            return socialhub_pb2.socialHubResponce()

    def postUserData(self, request, context):

        try:
            data = SocialHub(**MessageToDict(request)).postUserData()
            return socialhub_pb2.socialHubResponce(responce=json.dumps(data))

        except Exception as e:
            error_message = f"Error occurred while registering user: {str(e)}"
            logger.error(error_message)
            context.set_code(grpc.StatusCode.INTERNAL)
            context.set_details(error_message)
            return socialhub_pb2.socialHubResponce()

    # def register(self, request, context):
    #     oculus_user_service.UserService().registerUser(data=MessageToDict(request))


def server():
    _server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    socialhub_pb2_grpc.add_socialHubConnectorsServicer_to_server(SocialHubServer(), _server)
    _server.add_insecure_port('0.0.0.0:50051')
    _server.start()
    print('--------Server Started-----------')
    _server.wait_for_termination()


if __name__ == '__main__':
    print('--------Server Initiated-----------')
    server()
