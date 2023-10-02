import json
from concurrent import futures

import grpc
from google.protobuf.json_format import MessageToDict

from logs.studio_logger import Logger
from oculusservice.oculus_user_service import UserService as service
from protobufs import usermanagement_pb2_grpc, usermanagement_pb2
from socialhub.facebook import FaceBook
from socialhub.linkedIn import LinkedIn
from socialhub.twitter import Twitter
from connectors import SocialConnectors
logger = Logger("oculusUserManagement")


class UserManagement(usermanagement_pb2_grpc.oculusUserManagement):

    def register(self,request,context):
       try:
            return usermanagement_pb2.registraionResponce(registrationId=service().registerUser(data=self.__prepareDataForRegistration(MessageToDict(request))))
       except Exception as e:
           error_message = f"Error occurred while registering user: {str(e)}"
           logger.error(error_message)
           context.set_code(grpc.StatusCode.INTERNAL)
           context.set_details(error_message)
           return usermanagement_pb2.registraionResponce()



    def __prepareDataForRegistration(self, data):
        try:
            logger.info("Preparing data for register_user()...")
            data['faceBook'] = json.loads(FaceBook(**data['faceBook']).register_user())
            data['twitter'] = json.loads(Twitter(**data['twitter']).register_user())
            data['linkedIn'] = json.loads(LinkedIn(**data['linkedIn']).register_user())
            logger.info("Data for register_user() prepared...")
            return data
        except Exception as e:
            logger.error(str(e))


    def addPlatform(self,request,context):
        request=MessageToDict(request)
        if request['platformName']=='facebook':
            return usermanagement_pb2.platformResponce(media_responce=SocialConnectors.FaceBook(**request).register_connector())




def server():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    usermanagement_pb2_grpc.add_oculusUserManagementServicer_to_server(UserManagement(), server)
    server.add_insecure_port("[::]:50052")
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    print('--------UserManagementServer Started-----------')
    server()