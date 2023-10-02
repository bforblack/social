import json

from pydantic import BaseModel
from typing import Any, Optional
from socialhub.facebook import FaceBook
from socialhub.twitter import Twitter
from socialhub.instagram import Instagram
from socialhub.linkedin import LinkedIn

from logs.studio_logger import Logger
logger = Logger("socialHubIntegrationService")


class SocialHub(BaseModel):
    registrationId: str
    faceBook: Optional[FaceBook]
    instagram: Optional[Instagram]
    twitter: Optional[Twitter]
    linkedIn: Optional[LinkedIn]

    def getUserData(self):

        try:

            logger.info(f"Request for fetching data data for user_id: {self.registrationId} received...")

            self.faceBook = self.faceBook.getUserData()
            self.twitter = self.twitter.get_user_data()
            self.linkedIn = self.linkedIn.get_user_data()
            self.instagram = self.instagram.getUserData()

            logger.info(f"Request for fetching data data for user_id: {self.registrationId} completed...")

            return json.loads(self.json())

        except Exception as e:

            error_message = f"An Exception ocurred while fetching data for user_id: {self.registrationId}" \
                            f"error: {str(e)}"

            logger.error(error_message)
            return json.loads(self.json())

    def postUserData(self):

        try:

            logger.info(f"Request for posting data for user_id: {self.registrationId} received...")

            self.faceBook = self.faceBook.postUserData()
            self.twitter = self.twitter.post_tweet()
            self.linkedIn = self.linkedIn.post_data()
            self.instagram = self.instagram.postUserData()

            logger.info(f"Request for posting data for user_id: {self.registrationId} completed...")

            return json.loads(self.json())

        except Exception as e:

            error_message = f"An Exception ocurred while posting data for user_id: {self.registrationId}" \
                            f"error: {str(e)}"

            logger.error(error_message)
            return json.loads(self.json())












