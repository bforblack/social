import json
from pydantic import BaseModel
from typing import Any, Optional


class Twitter(BaseModel):
    # appId: Optional[str]
    # accessToken: str
    # Object: Optional[Any]

    bearerToken: Optional[Any]
    apiKey: Optional[Any]
    apiKeySecret: Optional[Any]
    accessToken: Optional[Any]
    accessTokenSecret: Optional[Any]
    Object: Optional[Any]

    def prepare_get_all_posts_data(self):
        self.Object = self._prepare_get_all_posts_data()
        return json.loads(self.json())

    def create_post_data(self, post_data):
        self.Object = self._create_post_data(post_data)
        return json.loads(self.json())

    @staticmethod
    def _prepare_get_all_posts_data():
        return json.dumps({"url": "https://api.twitter.com/2/tweets"})

    @staticmethod
    def _create_post_data(post_data):
        return json.dumps({"url": "https://api.twitter.com/2/tweets", "payload": {"text": post_data}})

    def prepare_get_single_post_data(self):
        self.Object = self._prepare_get_single_post_data()
        return json.loads(self.json())

    @staticmethod
    def _prepare_get_single_post_data():
        return json.dumps({"url": "https://api.twitter.com/2/tweets/"})
