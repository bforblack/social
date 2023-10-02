from pydantic import BaseModel
from typing import Any, Optional
from datetime import datetime
from database import mongo_connector as datasource
from linkedin_api.clients.restli.client import RestliClient
import json
class FaceBook(BaseModel):
    registrationId:str
    platformName:str
    data:Any
    registrationTime :datetime
    lastUpdatedTime :datetime

    def register_connector(self):
        if (self.__request_connector(params=self.__get_user_fields(),type='GET')):
            if(datasource.Mongo().update_one(id=self.registrationId,document={'facebook':json.loads(self.json(exclude={'registrationId','platformName'}))})):
                return self.json()
        else:
            return "Exception occured while registering Facebook connector for regsitrationId ="+self.registrationId

    def __get_user_fields(self):
        return "id,name,accounts{name,about,global_brand_page_name,access_token,category,connected_instagram_account,fan_count,features,followers_count,genre,has_whatsapp_business_number,instagram_business_account,business,tasks},business_users{first_name,id,last_name,business,assigned_pages{name,global_brand_page_name,category,id,access_token,connected_instagram_account,followers_count,has_whatsapp_business_number,instagram_business_account,permitted_tasks,tasks}}"




    def __request_connector(self,params,type):
        import requests
        URL="https://graph.facebook.com/v16.0/"+self.data['appId']
        try:
            if type == 'GET':
              URL = URL + '?fields=' + params + '& access_token=' + self.data['accesstoken']
              self.data=requests.get(url=URL).json()
            elif type == 'POST':
              self.data=requests.post(url=URL, params=params)
            return True
        except Exception as exception:
            print("Error")



class LinkedIn():
    #accesstoken:str
        def register_user(self):
            accesstoken = 'AQVIK6gIQaJbnwX6WNaQCviIOVC9urv4nDbaCjfTg7XkzMQTKCUjw9k9Wg8SuTj07dbCPS01fXLEWkGprwvVJQVfbcMhnipG1wLdySqSDaqZbcWsPSsyEQDC'
            RestliClient.get(access_token=accesstoken,resource_path='/me')
if __name__ == '__main__':
    accesstoken='AQVIK6gIQaJbnwX6WNaQCviIOVC9urv4nDbaCjfTg7XkzMQTKCUjw9k9Wg8SuTj07dbCPS01fXLEWkGprwvVJQVfbcMhnipG1wLdySqSDaqZbcWsPSsyEQDC-Nodl8SQgaYSIKHWzA_hKZ6WCC6aF_-vXc7yHBUVkg71UivrQWXXuOjXX8vL0E5UikQsXp4VJqIKcJB8yujTD_bh-WBLW4Aef9dzdMUSXDnLXA8tegdl6_6Q7bea5LStRH6rOZuWS3FLBCCasCpNKGnvJ8NB-hpbDf5Od4bqkICMTDFCNRo7-OalRaJ_vr0plHSx-PxS35tuwhEYaK6bpus0OvMirvotO12YEw'
    LinkedIn().register_user()
