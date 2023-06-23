import grpc
from concurrent import futures
import os
from google.protobuf.json_format import MessageToDict
from oculusservice.oculus_user_service import UserService as service
from protobufs import usermanagement_pb2_grpc,usermanagement_pb2
from pydantic import BaseModel
from typing import Optional
from socialhub.facebook_pojo import FaceBook
from socialhub.twitter_pojo import Twitter
from socialhub.linkedIn_pojo import LinkedIn
from socialhub.instagram_pojo import Instagram

class UserManagement(usermanagement_pb2_grpc.oculusUserManagement):



    def register(self,request,context):
       return usermanagement_pb2.registraionResponce(**service.registerUser( self.__prepareDataForRegistration(MessageToDict(request))))



    def __prepareDataForRegistration(self,data):
        if data['faceBook']!=None:
            data['faceBook']=FaceBook(**data['faceBook']).register_user()


        # Todo: create methods to support other platforms
        # if self.instagram != None:
        #     self.faceBook = self.instagram.register_user()




#
def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    usermanagement_pb2_grpc.add_oculusUserManagementServicer_to_server(UserManagement(), server)
    server.add_insecure_port("localhost:50052")
    server.start()
    server.wait_for_termination()




if __name__ == '__main__':
    print('--------UserManagementServer Started-----------')
    serve()
