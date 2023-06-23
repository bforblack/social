from pydantic import BaseModel
from typing import Any, Optional
from socialhub.oculusconnectorsapi import facebook_api
#update variables as per need

class Instagram(BaseModel):
    access_token: Any
    app_id: Any
    Object: Optional[Any]

    def getUserData(self, fields):
        return facebook_api.Facebook_graph_api(app_id=self.app_id, access_token=self.access_token,
                                               object=fields).getUserData()

    def postUserData(self, fields):
        return facebook_api.Facebook_graph_api(app_id=self.app_id, access_token=self.access_token,
                                               object=fields).postUserData()

