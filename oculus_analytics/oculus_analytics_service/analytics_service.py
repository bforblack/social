from pydantic import BaseModel
from typing import Any, Optional

class Analytics(BaseModel):
    userId:str
    socialmediaId:str
    mediaSource=str

    def postAnalytics(self):
        pass

    def userAnalytics(self):
        pass

    def trendAnalytics(self):
        pass

    def socialNetworkAnalytics(self):
        pass

    def audienceSegmentation(self):
        pass

    def generateReport(self):
        pass