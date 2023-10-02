from google.protobuf.json_format import MessageToDict
from pydantic import BaseModel,Field,Json
from typing import Optional,Any
from datetime import datetime
import random
from database import  mongo_connector as database
import logging
import json
from service import user_management
from database import mongo_connector as datasource

class User(BaseModel):
    registrationId:Optional[str]
    username:str
    email:str
    name:str
    mediaconnected:Optional[list]
    registration_time:Optional[datetime]
    last_updated_time:Optional[datetime]

    def process_user_registration(self):
     try:
         if self.registrationId is None:
             self.registrationId = 'OCULUS' + str(random.getrandbits(32))

         if self.registration_time is None:
            self.registration_time = datetime.now()

            self.last_updated_time = datetime.now()
         else:
             self.last_updated_time = datetime.now()

         if database.Mongo('user').save_data_user(json.loads(self.json())):
            return self.registrationId

     except Exception as exp:
         logging.error('Exception Caught While Registration of user for user = '+self.registrationId +' & username'+self.username,exp)
         return None

    def get_user(self,searchParamater):
        try:
            return User(datasource.Mongo('oculus').find(**searchParamater))
        except Exception :
            logging.error('Exception Caught While Fetching UserData')
            return None



class Media(BaseModel):
    registrationId:str
    platform_name:str
    data:Any
    registration_time: Optional[datetime]
    last_updated_time: Optional[datetime]

    def process_media_registration(self):
      try:
          if self.registration_time is None:
              self.registration_time = datetime.now()
              self.last_updated_time = datetime.now()
          return json.loads(MessageToDict(user_management.addPlatform(json.loads(self.json())))['mediaResponce'])










      except Exception as exp:
        logging.error('Exception Caught While Adding new Media of user with RegistrationId = ' + self.registrationId + ' & platformname' + self.platform_name,
                  exp)
        return None
