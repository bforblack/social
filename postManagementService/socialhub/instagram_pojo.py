import json

from pydantic import BaseModel
from typing import Any, Optional


class Instagram(BaseModel):
    appId: Optional[str]
    accessToken: Optional[str]
    Object: Optional[str]

    def getAllPostData(self):
        self.Object = self._getAllPostData()
        return json.loads(self.json())

    def getPostData(self):
        self.Object = self._getPostData()
        return json.loads(self.json())

    def _getAllPostData(self):
        return "posts{id,event,full_picture,message,message_tags,application,created_time,instagram_eligibility,is_expired}"

    def _getPostData(self):
        return "comments{from,id,message,like_count,user_likes,comment_count,reactions{id,name,pic_small,username},created_time,likes{id,name,pic_small}},likes{id,name,pic_small,username}"
