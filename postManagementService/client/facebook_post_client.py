import grpc
from protobufs import postmanagement_pb2_grpc
from protobufs import postmanagement_pb2


def make_call(stub):
    call = stub.createPost(postmanagement_pb2.postRequest(mediaSource="faceBook", pageId="100874061840165",
                                                          accessToken="EAALoMMkUPXEBOwhWJi78EG7hLdR0CZC5INfNEtzBF4LGwAXC00FyricjzuAWkrHvWY0W1cgaKeN2cw4FQOpPkTbt3C9kLnsZBGiF4ZBdeZCQ3fy4ZABg4RD4NVl4JbrEhV9gZCu4comankFXMaj3qwgZAXWezXrKZC4YfZBacEvFuYSIuEolgNaujSRxCZAfWUXI8ojBwxzIKkfkB50OyzsyZA7p4qOAlXUbvJGnhDLZA9IZD",
                                                          Object="{\"postData\":\"This is post from user\",\"process\":\"create\"}",
                                                          registrationId="110928107339307_223939389918466"))
    x = print(call)


def main():
    channel = grpc.insecure_channel('localhost:50053')
    stub = postmanagement_pb2_grpc.socialPostManagementStub(channel)
    make_call(stub)


if __name__ == "__main__":
    main()
