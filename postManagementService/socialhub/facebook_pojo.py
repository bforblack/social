import json
from typing import Any, Optional
from pydantic import BaseModel

from logs.studio_logger import Logger
logger = Logger("facebook pojo")


class FaceBook(BaseModel):
    appId: str
    accessToken: Optional[str]
    Object: Optional[Any]

    def getAllPostData(self):
        try:
            self.Object = self._getAllPostData()
            logger.info('Data prepared for all post')
            return json.loads(self.json())
        except Exception as e:
            logger.error(str(e))

    def createPostData(self, postData):
        try:
            self.Object = self._createPostData(postData)
            logger.info('data prepared for create post')
            return json.loads(self.json())
        except Exception as e:
            logger.error(str(e))

    def sharePostData(self, post_id):
        try:
            self.Object = self._sharePostData(post_id)
            logger.info('Data prepared for reshare post')
            return json.loads(self.json())
        except Exception as e:
            logger.error(str(e))

    def _getAllPostData(self):
        return "posts{id,event,full_picture,message,message_tags,application,created_time,instagram_eligibility,is_expired}"

    def _getPostData(self):
        return "message,comments{from,id,message,like_count,user_likes,comment_count,reactions{id,name,pic_small,username},created_time,likes{id,name,pic_small}},likes{id,name,pic_small,username}"

    def _createPostData(self, postData):
        return json.dumps({'connection': 'feed', 'message': postData})

    def _sharePostData(self, post_id):
        return json.dumps({'connection': 'feed', 'link': f'https://www.facebook.com/{self.appId}/posts/{post_id}'})

    def getPostData(self):
        self.Object = self._getPostData()
        return json.loads(self.json())
