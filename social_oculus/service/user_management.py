from protobufs import usermanagement_pb2_grpc,usermanagement_pb2
import os
import grpc

def registerUser(request):
    with grpc.insecure_channel(os.getenv("USER_MANAGEMENT")) as channel:
     return usermanagement_pb2_grpc.oculusUserManagementStub(channel).register(usermanagement_pb2.registraionRequest(**request))


def getUser(request):
    with grpc.insecure_channel(os.getenv("USER_MANAGEMENT")) as channel:
     return usermanagement_pb2_grpc.oculusUserManagementStub(channel).getUser(usermanagement_pb2.userInfoRequest(**request))


def addPlatform(request):
    with grpc.insecure_channel(os.getenv("USER_MANAGEMENT")) as channel:
        return usermanagement_pb2_grpc.oculusUserManagementStub(channel).addPlatform(
            usermanagement_pb2.platformRequest(**request))
