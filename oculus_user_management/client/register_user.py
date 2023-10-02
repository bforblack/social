import grpc
from protobufs import usermanagement_pb2_grpc, usermanagement_pb2


def make_call(stub):

    channel = grpc.insecure_channel('localhost:50051')

    stub = usermanagement_pb2_grpc.oculusUserManagementStub(channel)

    request = usermanagement_pb2.registraionRequest(
        registrationId='your_registration_id',
        faceBook=usermanagement_pb2.FaceBook(
            accessToken='your_facebook_access_token',
            appId='your_facebook_app_id'
        ),
        linkedIn=usermanagement_pb2.LinkedIn(
            appId='your_linkedin_app_id',
            accessToken='your_linkedin_access_token'
        ),
        twitter=usermanagement_pb2.Twitter(
            bearerToken='your_twitter_bearer_token',
            apiKey='your_twitter_api_key',
            apiKeySecret='your_twitter_api_key_secret',
            accessToken='your_twitter_access_token',
            accessTokenSecret='your_twitter_access_token_secret'
        ),
        instagram=usermanagement_pb2.Instagram(
            accessToken='your_instagram_access_token',
            appId='your_instagram_app_id'
        )
    )
    response = stub.register(request)

    return response

