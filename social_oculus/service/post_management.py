import json

from protobufs import postmanagement_pb2_grpc,postmanagement_pb2
import os
import grpc


def getAllPost(mediaSource,pageId,accessToken,registrationId):
    with grpc.insecure_channel(os.getenv("POST_MANAGEMENT")) as channel:
     return postmanagement_pb2_grpc.socialPostManagementStub(channel).getAllPost(postmanagement_pb2.getAllPostRequest
                                                                                 (registrationId=registrationId,
                                                                                  accessToken=accessToken,pageId=pageId,mediaSource=mediaSource))


# def postData(**request):
#     with grpc.insecure_channel(os.getenv("POST_MANAGEMENT")) as channel:
#      return postmanagement_pb2_grpc.socialPostManagementStub(channel).createPost(postmanagement_pb2.postRequest(**request))
#

def getPostedDataDetails(mediaSource,pageId,accessToken,registrationId):
    with grpc.insecure_channel(os.getenv("POST_MANAGEMENT")) as channel:
        return postmanagement_pb2_grpc.socialPostManagementStub(channel).getPost(
            postmanagement_pb2.getAllPostRequest(mediaSource=mediaSource,
                                                 pageId=pageId,accessToken=accessToken,registrationId=registrationId))


def createPost(registrationId,mediaSource,authData,pageId,postData):
    create_data = json.dumps({"postData": postData, "process": "create"})
    # print(create_data)
    with grpc.insecure_channel(os.getenv("POST_MANAGEMENT")) as channel:

        return postmanagement_pb2_grpc.socialPostManagementStub(channel).createPost(
            postmanagement_pb2.postRequest(mediaSource=mediaSource,
                                                 pageId=pageId, accessToken=authData, registrationId=registrationId,Object=create_data))
