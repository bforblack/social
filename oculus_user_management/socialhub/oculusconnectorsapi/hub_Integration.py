import json

from protobufs import socialhub_pb2_grpc,socialhub_pb2
import os
import grpc

def getUserData(request):
    with grpc.insecure_channel(os.getenv("SOCIALHUB")) as channel:
     return socialhub_pb2_grpc.socialHubConnectorsStub(channel).getUserData(socialhub_pb2.socialHubRequest(**json.loads(request)))



def postUserData(request):
    with grpc.insecure_channel(os.getenv("SOCIALHUB")) as channel:
        return socialhub_pb2_grpc.socialHubConnectorsStub(channel).postUserData(socialhub_pb2.socialHubRequest(**json.loads(request)))



