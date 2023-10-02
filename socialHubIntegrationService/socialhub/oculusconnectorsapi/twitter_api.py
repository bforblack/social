import requests
import json

from pydantic import BaseModel
from requests_oauthlib import OAuth1
from typing import Optional

from logs.studio_logger import Logger
logger = Logger("socialHubIntegrationService")


class TwitterAPI(BaseModel):
    bearerToken: Optional[str]
    apiKey: Optional[str]
    apiKeySecret: Optional[str]
    accessToken: Optional[str]
    accessTokenSecret: Optional[str]

    def get_user_data(self, url):
        try:
            auth = OAuth1(
                self.apiKey,
                self.apiKeySecret,
                self.accessToken,
                self.accessTokenSecret
            )

            response = requests.get(url, auth=auth)

            if response.status_code == 200:
                logger.info("Received successful response from get_user_data() call to Twitter API...")
                data = response.json()

                access_token = {
                    "bearerToken": self.bearerToken,
                    "apiKey": self.apiKey,
                    "apiKeySecret": self.apiKeySecret,
                    "accessToken": self.accessToken,
                    "accessTokenSecret": self.accessTokenSecret
                }

                access_token = json.dumps(access_token)
                data["accessToken"] = access_token

                return data
            else:
                logger.info(f"Received negative response from Twitter while making get_user_data() call to Twitter API: {response.text}")
                return {"error": response.text}

        except Exception as e:
            logger.info(f"An Exception occurred while making get_user_data() call to Twitter API: {str(e)}")
            return {"error": str(e)}

    def post_tweet(self, url, payload):
        try:
            auth = OAuth1(
                self.apiKey,
                self.apiKeySecret,
                self.accessToken,
                self.accessTokenSecret
            )
            response = requests.post(url, auth=auth, json=payload)

            if response.status_code == 201:
                logger.info("Received successful response from post_tweet() call to Twitter API...")
                tweet_data = response.json().get("data")
                return tweet_data

            else:
                logger.info(f"Received negative response from Twitter while making post_tweet() call to Twitter API: {response.text}")
                return {"error": response.text}

        except Exception as e:
            logger.info(f"An Exception occurred while making post_tweet() call to Twitter API: {str(e)}")
            return {"error": str(e)}

    def remove_tweet(self, url, tweet_id):
        try:
            auth = OAuth1(
                self.apiKey,
                self.apiKeySecret,
                self.accessToken,
                self.accessTokenSecret
            )

            delete_url = url + f"/{tweet_id}"
            headers = {"Authorization": "OAuth1"}
            response = requests.delete(delete_url, auth=auth, headers=headers)

            if response.status_code == 200:
                logger.info("Received successful response from delete_tweet() call to Twitter API...")
                return response.json()
            else:
                logger.info(f"Received negative response from Twitter while making delete_tweet() call to Twitter API: {response.text}")
                return {"error": response.text}

        except Exception as e:
            logger.info(f"An Exception occurred while making delete_tweet() call to Twitter API: {str(e)}")
            return {"error": str(e)}

    @staticmethod
    def get_posts():
        return {"posts": [], "error": "get_posts() endpoint is currently not available for Twitter"}
