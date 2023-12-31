# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import protobufs.socialhub_pb2 as socialhub__pb2


class socialHubConnectorsStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.getUserData = channel.unary_unary(
                '/protobufs.socialhubconnectors.socialHubConnectors/getUserData',
                request_serializer=socialhub__pb2.socialHubRequest.SerializeToString,
                response_deserializer=socialhub__pb2.socialHubResponce.FromString,
                )
        self.postUserData = channel.unary_unary(
                '/protobufs.socialhubconnectors.socialHubConnectors/postUserData',
                request_serializer=socialhub__pb2.socialHubRequest.SerializeToString,
                response_deserializer=socialhub__pb2.socialHubResponce.FromString,
                )


class socialHubConnectorsServicer(object):
    """Missing associated documentation comment in .proto file."""

    def getUserData(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def postUserData(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_socialHubConnectorsServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'getUserData': grpc.unary_unary_rpc_method_handler(
                    servicer.getUserData,
                    request_deserializer=socialhub__pb2.socialHubRequest.FromString,
                    response_serializer=socialhub__pb2.socialHubResponce.SerializeToString,
            ),
            'postUserData': grpc.unary_unary_rpc_method_handler(
                    servicer.postUserData,
                    request_deserializer=socialhub__pb2.socialHubRequest.FromString,
                    response_serializer=socialhub__pb2.socialHubResponce.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'protobufs.socialhubconnectors.socialHubConnectors', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class socialHubConnectors(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def getUserData(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/protobufs.socialhubconnectors.socialHubConnectors/getUserData',
            socialhub__pb2.socialHubRequest.SerializeToString,
            socialhub__pb2.socialHubResponce.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def postUserData(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/protobufs.socialhubconnectors.socialHubConnectors/postUserData',
            socialhub__pb2.socialHubRequest.SerializeToString,
            socialhub__pb2.socialHubResponce.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)
