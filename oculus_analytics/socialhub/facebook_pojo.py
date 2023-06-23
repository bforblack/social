from pydantic import BaseModel
from typing import Any, Optional
from oculusconnectorsapi import facebook_api

class FaceBook(BaseModel):
    app_id:str
    access_token:Optional[str]
    accounts:Optional[Any]
    business_users:Optional[Any]



