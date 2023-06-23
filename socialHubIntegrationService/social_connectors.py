import json

from pydantic import BaseModel
from typing import Any,Optional
from socialhub.facebook_pojo import FaceBook
from socialhub.twitter_pojo import Twitter
from socialhub.instagram_pojo import Instagram
from socialhub.linkedIn_pojo import LinkedIn

class SocialHub(BaseModel):
    userId:str
    faceBook:Optional[FaceBook]
    instagram:Optional[Instagram]
    twitter:Optional[Twitter]
    linkedIn:Optional[LinkedIn]




    def getUserData(self):
        #todo: similarly for LinkedIn and Twitter

        if self.faceBook!=None:
            self.faceBook=self.faceBook.getUserData()

        if self.instagram!=None:
            self.instagram=self.facebook.getUserData()

        if self.twitter != None:
           None

        if self.linkedIn!= None:
            None

        return self.json()










