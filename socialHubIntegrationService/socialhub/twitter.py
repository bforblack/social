import json

from pydantic import BaseModel
from typing import Any, Optional
from socialhub.oculusconnectorsapi.twitter_api import TwitterAPI

from logs.studio_logger import Logger
logger = Logger("socialHubIntegrationService")


class Twitter(BaseModel):
    bearerToken: Optional[str]
    apiKey: Optional[str]
    apiKeySecret: Optional[str]
    accessToken: Optional[str]
    accessTokenSecret: Optional[str]
    Object: Optional[str]

    # def get_user_data(self):
    #     empty_fields = [field_name for field_name in ["apiKey", "apiKeySecret",
    #                                                   "accessToken", "accessTokenSecret", "Object"]
    #                     if not getattr(self, field_name) or getattr(self, field_name, '').strip() == '']
    #
    #     if len(empty_fields) == 5:
    #         return {}
    #
    #     elif empty_fields:
    #         error = f"The following fields cannot be empty: {', '.join(empty_fields)}"
    #         logger.info(f"An exception occurred while registering Twitter user: {error}")
    #         error_message = {"error": error}
    #         return error_message
    #
    #     else:
    #         _object = json.loads(self.Object)
    #         service = _object.get('service')
    #
    #         if service == 'oculus_user_management':
    #             url = _object.get('url')
    #             response = TwitterAPI(apiKey=self.apiKey,
    #                                   apiKeySecret=self.apiKeySecret,
    #                                   accessToken=self.accessToken,
    #                                   accessTokenSecret=self.accessTokenSecret).get_user_data(url=url)
    #
    #             if not response.get('error_message'):
    #                 access_token = {
    #                     "bearerToken": self.bearerToken,
    #                     "apiKey": self.apiKey,
    #                     "apiKeySecret": self.apiKeySecret,
    #                     "accessToken": self.accessToken,
    #                     "accessTokenSecret": self.accessTokenSecret
    #                 }
    #
    #                 access_token = json.dumps(access_token)
    #
    #                 data = {"accessToken": access_token, "id": response.get("data").get("id"),
    #                         "name": response.get("data").get("name"), "username": response.get("data").get("username")}
    #
    #                 return data
    #
    #             else:
    #                 return response
    #
    #         elif service == 'oculus_post_management':
    #             response = TwitterAPI(apiKey=self.apiKey,
    #                                   apiKeySecret=self.apiKeySecret,
    #                                   accessToken=self.accessToken,
    #                                   accessTokenSecret=self.accessTokenSecret).get_posts()
    #
    #             return response

    def get_user_data(self):
        empty_fields = [field_name for field_name in ["apiKey", "apiKeySecret",
                                                      "accessToken", "accessTokenSecret", "Object"]
                        if not getattr(self, field_name) or getattr(self, field_name, '').strip() == '']

        if len(empty_fields) == 5:
            return {}

        elif empty_fields:
            error = f"The following fields cannot be empty: {', '.join(empty_fields)}"
            logger.info(f"An exception occurred while registering Twitter user: {error}")
            error_message = {"error": error}
            return error_message

        else:
            _object = json.loads(self.Object)
            url = _object.get('url')
            response = TwitterAPI(bearerToken=self.bearerToken,
                                  apiKey=self.apiKey,
                                  apiKeySecret=self.apiKeySecret,
                                  accessToken=self.accessToken,
                                  accessTokenSecret=self.accessTokenSecret).get_user_data(url=url)

            return response

    def post_tweet(self):
        empty_fields = [field_name for field_name in ["apiKey", "apiKeySecret",
                                                      "accessToken", "accessTokenSecret", "Object"]
                        if not getattr(self, field_name) or getattr(self, field_name, '').strip() == '']

        if len(empty_fields) == 5:
            return {}

        elif empty_fields:
            error = f"The following fields cannot be empty: {', '.join(empty_fields)}"
            logger.info(f"An exception occurred while posting data on Twitter: {error}")
            error_message = {"error": error}
            return error_message

        else:
            try:
                _object = json.loads(self.Object)
                url = _object.get('url')
                payload = _object.get('payload')
                return TwitterAPI(apiKey=self.apiKey,
                                  apiKeySecret=self.apiKeySecret,
                                  accessToken=self.accessToken,
                                  accessTokenSecret=self.accessTokenSecret).post_tweet(url=url, payload=payload)

            except Exception as e:
                logger.info(f"An exception occurred while posting data on Twitter: {e}")
                error_message = {"error": e}
                return error_message

    def delete_tweet(self):
        empty_fields = [field_name for field_name in ["apiKey", "apiKeySecret",
                                                      "accessToken", "accessTokenSecret", "Object"]
                        if not getattr(self, field_name) or getattr(self, field_name, '').strip() == '']

        if len(empty_fields) == 5:
            return {}

        elif empty_fields:
            error = f"The following fields cannot be empty: {', '.join(empty_fields)}"
            logger.info(f"An exception occurred while deleting post from Twitter: {error}")
            error_message = {"error": error}
            return error_message

        else:
            try:
                _object = json.loads(self.Object)
                tweet_id = _object.get("post_id")
                url = _object.get("url")
                return TwitterAPI(apiKey=self.apiKey,
                                  apiKeySecret=self.apiKeySecret,
                                  accessToken=self.accessToken,
                                  accessTokenSecret=self.accessTokenSecret).remove_tweet(url=url,
                                                                                         tweet_id=tweet_id)

            except Exception as e:
                logger.info(f"An exception occurred while posting data on Twitter: {e}")
                error_message = {"error": e}
                return error_message


