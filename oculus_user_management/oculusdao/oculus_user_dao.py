from pydantic import BaseModel
from typing import Any, Optional
from socialhub import facebook_pojo,twitter_pojo,linkedIn_pojo,instagram_pojo
from database.mongo_connector import Mongo
import json

class User(BaseModel):
    username: Optional[str]
    userId: Optional[str]
    faceBook: Optional[facebook_pojo.FaceBook]
    twitter: Optional[twitter_pojo.Twitter]
    linkedin: Optional[linkedIn_pojo.LinkedIn]
    instagram:Optional[instagram_pojo.Instagram]


    def register(self):
        return Mongo.save_data(collectionName='user',document=json.loads(self.json()))

    #Todo other CRUD tasks

    def getUser(self,userId):
        pass
