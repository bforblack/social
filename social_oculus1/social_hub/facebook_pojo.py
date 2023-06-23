from oculus_api import facebook_api
from pydantic import BaseModel
from typing import Any, Optional


class FaceBook(BaseModel):
    app_id:str
    access_token:Optional[str]
    accounts:Optional[Any]
    business_users:Optional[Any]




    def register_user(self):
        return facebook_api.Facebook_graph_api(app_id=self.app_id, access_token=self.access_token).getUserData()

    def post_data(self,message):
        for x in self.accounts['data']:
                            if x['id']==self.app_id:
                                self.access_token= x['access_token']

        return facebook_api.Facebook_graph_api(app_id=self.app_id, access_token=self.access_token).post_data(message)

    def delete(self,id):
        return facebook_api.Facebook_graph_api(app_id=self.app_id, access_token=self.access_token).removePost(id)



















