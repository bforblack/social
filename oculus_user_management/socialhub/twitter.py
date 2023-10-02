from pydantic import BaseModel
from typing import Any, Optional
import json


class Twitter(BaseModel):
    bearerToken: Optional[str]
    apiKey: Optional[str]
    apiKeySecret: Optional[str]
    accessToken: Optional[str]
    accessTokenSecret: Optional[str]
    Object: Optional[str]

    def register_user(self):
        self.Object = self.__get_user_fields()
        return self.json()

    @staticmethod
    def __get_user_fields():
        return json.dumps({"url": "https://api.twitter.com/2/users/me"})
