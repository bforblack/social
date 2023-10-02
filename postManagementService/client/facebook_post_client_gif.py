import grpc
from protobufs import postmanagement_pb2_grpc
from protobufs import postmanagement_pb2


def make_call(stub):

    call = stub.createPost(postmanagement_pb2.postRequest(mediaSource="faceBook",
                                                          pageId="103658366092003",
                                                          accessToken="EAAathGdn1gcBO2nfgPVBAkAmTgZA6TFfrKpKCXBCPmA2hcZAZCC9IBWqmb1brhzNbMJ2UAwGIPSXmiSGrmr1ZCCuXD295C4ktlxFLjMCZA9bJptBldaJkATNg63rKjYEZBdULFQKMPDdfZCMpRf8YhZBIPaJb5k3ZBiLHwpLymeMwVQVbMB4H3zhBdmaGYB8EpiGWi8EvkZBkZD",
                                                          Object="{\"post\":\"This is post from user\",\"gif_title\":\"Gif Title\",\"process\":\"create\",\"mediaType\":\"gif\"}",
                                                          registrationId="110928107339307_223939389918466"))

    print(call)


def main():
    channel = grpc.insecure_channel('0.0.0.0:50053')
    stub = postmanagement_pb2_grpc.socialPostManagementStub(channel)
    make_call(stub)


if __name__ == "__main__":
    main()
