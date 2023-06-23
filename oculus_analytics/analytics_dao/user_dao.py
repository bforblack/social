from pydantic import BaseModel
from typing import Any, Optional

class UserDao(BaseModel):
    userID:str
    socialmediaId:str
    mediaSource:int


    #def get_post_related_data(self):


