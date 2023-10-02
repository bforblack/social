from pydantic import BaseModel
from typing import Any, Optional
import json


class LinkedIn(BaseModel):
    accessToken: Optional[str]
    appId: Optional[str]
    Object: Optional[str]

    def register_user(self):
        self.Object = self.__get_user_fields()
        return self.json()

    def __get_user_fields(self):
        return json.dumps({"url": "https://api.linkedin.com/v2/me"})
