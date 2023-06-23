import concurrent.futures as futures

import grpc

from protobufs import socialhub_pb2_grpc
from social_connectors import SocialHub
from google.protobuf.json_format import MessageToDict

class SocialHubServer(socialhub_pb2_grpc.socialHubConnectors):

    def getUserData(self,request,context):
        return SocialHub(**MessageToDict(request)).getUserData()

    # def postUserData(self,request):
    #     return SocialHub(**MessageToDict(request)).get()


    # def register(self, request, context):
    #     oculus_user_service.UserService().registerUser(data=MessageToDict(request))
def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    socialhub_pb2_grpc.add_socialHubConnectorsServicer_to_server(SocialHubServer(), server)
    server.add_insecure_port("localhost:50051")
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    print('--------Server Started-----------')
    serve()
