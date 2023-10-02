import grpc
from protobufs import postmanagement_pb2_grpc
from protobufs import postmanagement_pb2


def make_call(stub):
    call = stub.getAllPost(postmanagement_pb2.getAllPostRequest(mediaSource="twitter", pageId="77nxbb4joerbfe",
                                                                accessToken="{\"bearerToken\":\"AAAAAAAAAAAAAAAAAAAAAO5anwEAAAAAAg7Yq3LHcT8GHU9CdUM9Xdnx%2Bpk%3DUw9bVcY62kCdBrMvPLpumrceyWCpDcv8ThyNd5L8ibHRVukxXq\",\"apiKey\":\"rlK5eBq5FiaCjIl1HNQYj8tIl\",\"apiKeySecret\":\"9VCDYva7ymUtFhukFoZJksr2BKoIXm4zFpLbwIym6ikWKEssRH\",\"accessToken\":\"1660903613076758528-rGhNMF88anjfG0GpVnpfNYZY9RQl1J\",\"accessTokenSecret\":\"oy761O8aJqCW1mdfqGBAuak2gULNA5t4NXJhTLLkoNDfK\"}",
                                                                registrationId="110928107339307_223939389918466"))
    x = print(call)


def main():
    channel = grpc.insecure_channel('0.0.0.0:50053')
    stub = postmanagement_pb2_grpc.socialPostManagementStub(channel)
    make_call(stub)


if __name__ == "__main__":
    main()
