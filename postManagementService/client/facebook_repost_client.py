import grpc
from protobufs import postmanagement_pb2_grpc
from protobufs import postmanagement_pb2


def make_call(stub):
    # call = stub.createPost(postmanagement_pb2.postRequest(mediaSource="faceBook", pageId="100874061840165",
    #                                                     accessToken="EAALoMMkUPXEBO2SLFMonw7IVZCfgcKZAWPGEGrFkTyTz2CljIKobEp5Fsq7HMSCgP5OAUrDwmn70ydHkPuhAorhKu32NxXEZCa7dCx6xOE1s0Rx8ZB7AOykzgTRA0lgKcZClWsyznMbk6BQ1eg8qbxYRE5S4jS2LEjC4aINTJgQfFkL89PIrxKaWsd4RsnEXNGblnFgpRCwc17syBdO2OxNPrxpErucYn7fTFLkCi",
    #                                                     registrationId="110928107339307_223939389918466",
    #                                                     Object="{\"post_id\":\"100874061840165_746194503974781\",\"message\":null,\"process\":\"repost\"}"))

    call = stub.postSchedule(postmanagement_pb2.postRequest(mediaSource="faceBook", pageId="100874061840165",
                                                          accessToken="EAALoMMkUPXEBO2SLFMonw7IVZCfgcKZAWPGEGrFkTyTz2CljIKobEp5Fsq7HMSCgP5OAUrDwmn70ydHkPuhAorhKu32NxXEZCa7dCx6xOE1s0Rx8ZB7AOykzgTRA0lgKcZClWsyznMbk6BQ1eg8qbxYRE5S4jS2LEjC4aINTJgQfFkL89PIrxKaWsd4RsnEXNGblnFgpRCwc17syBdO2OxNPrxpErucYn7fTFLkCi",
                                                          registrationId="110928107339307_223939389918466",
                                                          Object="{\"post_id\":\"100874061840165_746194503974781\",\"message\":null,\"process\":\"repost\",\"schedule_time\":\"19:01\"}"))
    # post_time="10:40"))
    # ,schedule_time="12:51"))
    x = print(call)


def main():
    channel = grpc.insecure_channel('localhost:50053')
    stub = postmanagement_pb2_grpc.socialPostManagementStub(channel)
    make_call(stub)


if __name__ == "__main__":
    main()
