from pydantic import BaseModel
from typing import Any, Optional
from socialhub.oculusconnectorsapi import facebook_api

class FaceBook(BaseModel):
    appId:str
    accessToken:str
    accounts:Optional[Any]
    businessUsers:Optional[Any]
    Object:Optional[Any]



    #Todo: CRUD opertaions
    def getUserData(self):
        return facebook_api.Facebook_graph_api(app_id=self.appId, access_token=self.accessToken,object=self.Object).getUserData()


    def postUserData(self):
        return facebook_api.Facebook_graph_api(app_id=self.appId, access_token=self.accessToken,object=self.Object).postUserData()


