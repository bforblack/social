import json
from protobufs import socialhub_pb2_grpc, socialhub_pb2
import os
import grpc

from logs.studio_logger import Logger
logger = Logger("oculusUserManagement")


def getUserData(request):
    try:
        logger.info(f"Sending request to socialhub grpc server to get_user_data() for user (user_id: {request['registrationId']})...")
        with grpc.insecure_channel(os.getenv("SOCIALHUB")) as channel:
            response = socialhub_pb2_grpc.socialHubConnectorsStub(channel).getUserData(socialhub_pb2.socialHubRequest(**request))
            logger.info(f"Received response from socialhub grpc server for get_user_data() for user (user_id: {request['registrationId']})...")
            return response
    except Exception as e:
        logger.error(str(e))


def postUserData(request):
    try:
        logger.info(f"Sending request to socialhub grpc server to post_user_data() for user (user_id: {request['registrationId']})...")
        with grpc.insecure_channel(os.getenv("SOCIALHUB")) as channel:
            response = socialhub_pb2_grpc.socialHubConnectorsStub(channel).postUserData(socialhub_pb2.socialHubRequest(**json.loads(request)))
            logger.info(f"Sending request to socialhub grpc server to post_user_data() for user (user_id: {request['registrationId']})...")
            return response
    except Exception as e:
        logger.error(str(e))


