import grpc
from protobufs import postmanagement_pb2_grpc
from protobufs import postmanagement_pb2


def make_call(stub):
    call = stub.getAllPost(postmanagement_pb2.getAllPostRequest(mediaSource="faceBook",
                                                                pageId="100874061840165",
                                                                accessToken="EAALoMMkUPXEBO2yMB1ZABoFZCrVnxTvCriChIm12BKz4lCLgAOmCqz5vs4wu6xOefwsBZC5ZB7nkj8ZCwEbCkn76Muwa2kSUu4GKjpf7tTChHNdZCI8V8fRJjnropzXFgoNeK5ZBE0c1I0x0Ht1O4lKTPYW50TelZBu4xi76XFra4EJqhXbYhMWZBSo8YdYV1BQSj1YeGoS1GKpzZAzbdgg4RDBuE1nZC1MqOxTEvQRTKAZD",
                                                                registrationId="110928107339307_223939389918466"))
    print(call)


def main():
    channel = grpc.insecure_channel('0.0.0.0:50053')
    stub = postmanagement_pb2_grpc.socialPostManagementStub(channel)
    make_call(stub)


if __name__ == "__main__":
    main()
