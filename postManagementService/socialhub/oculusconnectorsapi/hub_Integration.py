import json
from protobufs import socialhub_pb2_grpc, socialhub_pb2
import os
import grpc
from dotenv import load_dotenv
load_dotenv()

from logs.studio_logger import Logger
logger = Logger("postManagementService")


def getUserData(request):
    logger.info("Sending request to socialhub grpc server to get_user_data()...")
    try:
        with grpc.insecure_channel(os.getenv("SOCIALHUB")) as channel:
            response = socialhub_pb2_grpc.socialHubConnectorsStub(channel).getUserData(socialhub_pb2.socialHubRequest(**json.loads(request)))
            logger.info("Received response from socialhub grpc server for get_user_data()...")
            return response
    except Exception as e:
        logger.error(str(e))


def postUserData(request):
    logger.info("Sending request to socialhub grpc server to post_user_data()...")
    try:
        with grpc.insecure_channel(os.getenv("SOCIALHUB")) as channel:
            response = socialhub_pb2_grpc.socialHubConnectorsStub(channel).postUserData(socialhub_pb2.socialHubRequest(**json.loads(request)))
            logger.info("Received response from socialhub grpc server for post_user_data()...")
            return response
    except Exception as e:
        logger.error(str(e))



