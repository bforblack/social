from pydantic import BaseModel
from typing import Any, Optional
from socialhub.oculusconnectorsapi import facebook_api


class Instagram(BaseModel):
    accessToken: Optional[str]
    appId: Optional[str]
    Object: Optional[str]

    # def getUserData(self, fields):
    #     return facebook_api.Facebook_graph_api(app_id=self.appId, access_token=self.accessToken,
    #                                            object=fields).getUserData()
    #
    # def postUserData(self, fields):
    #     return facebook_api.Facebook_graph_api(app_id=self.appId, access_token=self.accessToken,
    #                                            object=fields).postUserData()

    def getUserData(self):

        empty_fields = [field_name for field_name in ["appId", "accessToken", "Object"]
                        if not getattr(self, field_name) or getattr(self, field_name, '').strip() == '']

        return {}

    def postUserData(self):

        empty_fields = [field_name for field_name in ["appId", "accessToken", "Object"]
                        if not getattr(self, field_name) or getattr(self, field_name, '').strip() == '']

        return {}
