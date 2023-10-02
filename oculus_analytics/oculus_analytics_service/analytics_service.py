from analytics_dao import user_dao
import pandas as pd
from nlu_service import pre_trained_model
from socialhub.oculusconnectorsapi import hub_Integration
from socialhub.facebook_pojo import  FaceBook
from socialhub.linkedIn_pojo import  LinkedIn
from socialhub.twitter_pojo import  Twitter
from socialhub.instagram_pojo import Instagram
from oculus_analytics_service import report_generator



class Analytics:


    def postAnalytics(self,data):
        data =user_dao.Post(**data).get_post_related_data()
        #hub_Integration.getUserData(user_dao.Post(**data).get_post_related_data())
        processedData=_prepareDataForProcessing(data)
        sentime,ner=_compute(pre_trained_model.getPipeline(),processedData['message'])
        finaldata=processedData.merge(pd.DataFrame(sentime),right_index=True,left_index=True)
        finaldata=finaldata.merge(pd.DataFrame(ner), right_index=True, left_index=True)
        report=report_generator.createSentimentChart(finaldata)
        return report,finaldata.to_json
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


def _prepareDataForProcessing(data)->pd.DataFrame:
    return pd.DataFrame.from_records(data['Object']['faceBook']['comments']['data'])


def _compute(pipeLine,data):
    sentiments=pipeLine['sentiment'](list(data))
    ner=pipeLine['ner'](list(data))
    return sentiments,ner


def __prepareDataForPost( data):
        processedData = {'registrationId': data["registrationId"],
                         'faceBook': {'appId': 'None', 'accessToken': 'None', 'Object': 'None'}, 'instagram': {},
                         'twitter': {'bearerToken': 'None',
                                     'apiKey': 'None',
                                     'apiKeySecret': 'None',
                                     'accessToken': 'None',
                                     'accessTokenSecret': 'None',
                                     'Object': 'None'}, 'linkedIn': {'appId': 'None',
                                                                     'accessToken': 'None',
                                                                     'Object': 'None'}}

        if data['mediaSource'] == 'faceBook':
            processedData['faceBook'] = FaceBook(appId=data['pageId'], accessToken=data['accessToken']).getAllPostData()
        elif data['mediaSource'] == 'twitter':
            processedData['twitter'] = Twitter(bearerToken=data['bearerToken'], apiKey=data['apiKey'],
                                               apiKeySecret=data['apiKeySecret'], accessToken=data['accessToken'],
                                               accessTokenSecret=data['accessTokenSecret']).getAllPostData()
        elif data['mediaSource'] == 'linkedIn':
            processedData['linkedIn'] = LinkedIn(accessToken=data['accessToken'], appId=data['pageId']).getAllPostData()

        # json_string = json.dumps(processedData)
        # return json_string
        return processedData