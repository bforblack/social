from pydantic import BaseModel
from typing import Any, Optional
from database.mongo_connector import Mongo
from socialhub.oculusconnectorsapi import hub_Integration
import json
import random
import datetime

class User(BaseModel):
    username:str
    registrationId: Optional[str]
    faceBook: Optional[Any]
    twitter: Optional[Any]
    linkedIn: Optional[Any]
    instagram:Optional[Any]
    registrationTime:Optional[Any]
    lastUpatedTime:Optional[Any]



    def register(self):
        self.registrationId='OCULUS'+str(random.getrandbits(32))
        self.registrationTime=datetime.datetime.now()
        self.lastUpatedTime = datetime.datetime.now()
        data=json.loads(hub_Integration.getUserData(json.loads(self.json(exclude={'username','registrationTime','lastUpatedTime'}))).responce)
        self.faceBook=data['faceBook']
        self.twitter=data['twitter']
        self.linkedIn=data['linkedIn']
        if(Mongo().save_data(collectionName='user',document=json.loads(self.json()))):
            return self.registrationId
        else:
            return 'False'


    #Todo other CRUD tasks

    def getUser(self,userId):
        pass
