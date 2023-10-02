import grpc
from protobufs import postmanagement_pb2_grpc
from protobufs import postmanagement_pb2


def make_call(stub):
    call = stub.getPost(postmanagement_pb2.getAllPostRequest(mediaSource="faceBook",
                                                                pageId="100874061840165_746783910582507",
                                                                accessToken="EAALoMMkUPXEBO03CDyWJTVBRPC7RrSZBUPWubW6ZB0GBX4rbDZBpqZClLe3XxMLCbvKSzwtmJ9QgZCOmroyodwBeP1boPyZB21ZBDvsLWZCGrY5NcU1TZAVKwxZBI8C7diLH2ZAnVt4w3H9Hjo92fLaFTZCRaw4oPXXbWgL4obai6Tmja7fEvrHHZAhXtj2eN0tx8ZBeKzGZC7r1WiAvAakqQPxGgp9DssK5ZBZAsv6L6by1erxoZD",
                                                                registrationId="110928107339307_223939389918466"))
    print(call)


def main():
    channel = grpc.insecure_channel('localhost:50053')
    stub = postmanagement_pb2_grpc.socialPostManagementStub(channel)
    make_call(stub)


if __name__ == "__main__":
    main()
