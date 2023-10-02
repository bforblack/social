import grpc
import json

from protobufs import postmanagement_pb2_grpc
from protobufs import postmanagement_pb2


def make_call(stub):
    call = stub.getAllPost(postmanagement_pb2.getAllPostRequest(mediaSource="linkedIn",
                                                                pageId="96072893",
                                                                accessToken="AQX_qX5ti8iEIo5tuuNa2jarpRtxcnylBDR9ylI6oT2sdxLju-lTK8w0RUSFMuo31qIRF_DJ56J9YcA-DPDL1SAX-FYiDiMzgwwoDwJDimoxwHbQKpPrvd0ZdlF7v05Vv0JEG_wg3RaNR2Xt5QlU86GYx9a_-ZolTgA5Env_wkN4wcoUuhPOpxsBNSec5y8cHD9zw7i1RHIm3Tc8bcQN_IxOrX4mLLsgSLrDYrI_dJoWfVv6oBx6JGYCjj_4_AyAyC5o89PHjK7lye5stK9DCgAZ7i2lVeW6PnCmvuR0RAv0Is9-2Q7ZJYBdk09QRPYDJpoczGckdGCfWgqJyUGHvg2Uqmlz4Q",
                                                                registrationId="110928107339307_223939389918466"))
    print(call)


def main():
    channel = grpc.insecure_channel('0.0.0.0:50053')
    stub = postmanagement_pb2_grpc.socialPostManagementStub(channel)
    make_call(stub)


if __name__ == "__main__":
    main()
