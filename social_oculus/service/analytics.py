from protobufs import oculus_analytics_pb2_grpc,oculus_analytics_pb2
import os
import grpc

def getPostReport(**request):
    with grpc.insecure_channel(os.getenv("ANALYTICS_MANAGEMENT")) as channel:
     return oculus_analytics_pb2_grpc.oculusAnalyticsStub(channel).postAnalytics(oculus_analytics_pb2.userPostRequest(**request))
