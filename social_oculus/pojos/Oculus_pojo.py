from bson.objectid import  ObjectId
from pydantic import BaseModel,Field,Json
from typing import Optional,Any

from oculus_source import source_connector
from social_hub import facebook_pojo,linkedin_pojo
import json
from bson import json_util





class Oculus(BaseModel):
    username:Optional[str]
    _id:Optional[str]
    face_book:Optional[Any]
    twitter:Optional[Any]
    linkedin:Optional[Any]


    def registerUser(self):
        return self._process_user_request()


    def _process_user_request(self):
        if self.face_book is not None:
            self.face_book=facebook_pojo.FaceBook(**self.face_book).register_user()

    #Todo : self.twitter

        if self.linkedin is not None:
            self.linkedin=linkedin_pojo.Linkedin(**self.linkedin).register_user()


        return self._save_data()


    def _save_data(self):
       return str(source_connector.get_data_base_connector().get_database('social').get_collection('user').insert_one(
            json.loads(self.json())).inserted_id)



    def get_user(self,id):
        return json.loads(json_util.dumps(source_connector.get_data_base_connector().get_database('social').\
            get_collection('user').find_one({'_id':ObjectId(id)})))


    def post_data(self,id,object,request):
        return facebook_pojo.FaceBook(**self.get_user(id)[object],app_id=request['id']).post_data(request['post'])

      #return None
    def report(self,id,object,request):
        user_data=facebook_pojo.FaceBook(**self.get_user(id)[object],app_id=request['id']).getposts()
        return

    def report(self, id,object,mediaId):
        user_data = facebook_pojo.FaceBook(**self.get_user(id)[object],app_id=mediaId)
        return

    def getPosts(self,id,pageId):
        user_data=self.get_user(id)


