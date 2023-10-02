from protobufs import oculus_analytics_pb2,oculus_analytics_pb2_grpc
import grpc
import concurrent.futures as futures
from oculus_analytics_service import analytics_service
from google.protobuf.json_format import MessageToDict


class AnalyticsService(oculus_analytics_pb2_grpc.oculusAnalytics):

   def  postAnalytics(self,request,context):
     report,data = analytics_service.Analytics().postAnalytics(MessageToDict(request))
     oculus_analytics_pb2.userResponce(processedReportData=str(report),processedReportId=str(data))










def server():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    oculus_analytics_pb2_grpc.add_oculusAnalyticsServicer_to_server(AnalyticsService(), server)
    server.add_insecure_port("localhost:50054")
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    print('--------Analytics Server Started-----------')
    server()