from pydantic import BaseModel
from typing import Any, Optional
from database import mongo_connector
from bson.objectid import ObjectId



class Post(BaseModel):
    id:Optional[Any]
    pageId:str
    registrationId:str


    def get_post_related_data(self):
      if self.id!=None:
        self.id=ObjectId(self.id)
        data=mongo_connector.Mongo().find_data(collectionName='post',document={"_id":self.id})

      return data







