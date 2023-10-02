import json
from logs.studio_logger import Logger

logger = Logger("linkedin pojo")
from pydantic import BaseModel
from typing import Any, Optional


class LinkedIn(BaseModel):
    accessToken: Optional[str]
    appId: Optional[str]
    Object: Optional[str]

    def prepare_get_all_posts_data(self):
        try:
            self.Object = self._prepare_get_all_posts_data()
            logger.info(f'Data prepared for all post')
            return json.loads(self.json())
        except Exception as e:
            logger.error(str(e))

    def _prepare_get_all_posts_data(self):
        start = 0
        author = f"urn:li:organization:{self.appId}"
        url = self._prepare_get_all_posts_url(start, author)
        return json.dumps({"url": url})

    def sharePostData(self, post_id, message):
        try:
            self.Object = self._sharePostData(post_id, message)
            logger.info('Data prepared for reshare post')
            return json.loads(self.json())
        except Exception as e:
            logger.error(str(e))

    @staticmethod
    def _prepare_get_all_posts_url(start, author):
        url = f"https://api.linkedin.com/v2/posts?q=author&author={author}&start={start}&count=10"
        return url

    def create_post_data(self, post_message):
        self.Object = self._create_post_data(post_message)
        return json.loads(self.json())

    def _create_post_data(self, post_message):
        return json.dumps({"url": "https://api.linkedin.com/v2/posts",
                           "payload": {"author": f"urn:li:organization:{self.appId}", "post": post_message}})

    def prepare_get_single_post_data(self):
        self.Object = self._prepare_get_single_post_data()
        return json.loads(self.json())

    def _prepare_get_single_post_data(self):
        url = f"https://api.linkedin.com/v2/posts/{self.appId}"
        return json.dumps({"url": url})

    def _sharePostData(self, post_id, message):
        return json.dumps({"url": "https://api.linkedin.com/rest/posts",
                           "payload": {"author": f"urn:li:organization:{self.appId}", "parent": post_id,
                                       "message": message, "mediaType": "reshare"}})
