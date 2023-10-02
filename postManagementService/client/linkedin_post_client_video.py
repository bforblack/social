import grpc
from protobufs import postmanagement_pb2_grpc
from protobufs import postmanagement_pb2


def make_call(stub):

    call = stub.createPost(postmanagement_pb2.postRequest(mediaSource="linkedIn",
                                                          pageId="96072893",
                                                          accessToken="AQUbm7y21qwnzeBnN1grSOlE5UEodWPh3gQ8wFDK94BhgLA3Gmi0LNX9UPByHthZvVlkagxT7DHp_ONSFc4uhqXApnHrO2ASo6J5_4jSzvFp4EZeWsflqdjQWHy0g3mZ7CcOtNERoWiXg6_jPVY8nXPA55gIIu9z8EERRcLYNRrOP3QZQjzRdrWd4VQeWyEeuFcCjrO4Vfg8NyxN-Dgy8jBpPiczbXyhHXBBGssdrpFmcK5Z24X-NzBq3a2GfYRaUeOLFOmnhoELFmwGt1d8ghEDRn4-HFitCMUR1i08u82Px-CJYP8a7oqOq1IuXBHTwzwx6aK1b5ypWBlUCvSd4R3CbTo5kQ",
                                                          Object="{\"post\":\"This is post from user...\",\"process\":\"create\",\"mediaType\":\"video\"}",
                                                          registrationId="110928107339307_223939389918466"))

    print(call)


def main():
    channel = grpc.insecure_channel('0.0.0.0:50053')
    stub = postmanagement_pb2_grpc.socialPostManagementStub(channel)
    make_call(stub)


if __name__ == "__main__":
    main()
