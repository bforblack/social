from pydantic import BaseModel
from typing import Optional,Any
from database import mongo_connector
import json
from datetime import datetime
from logs.studio_logger import Logger
logger = Logger("postManagementService")


class UserPostDao(BaseModel):
    id: Optional[str]
    registrationId: Optional[str]
    Object: Optional[Any]
    postFetchedTime: Optional[Any]
    post_last_updated_time: Optional[Any]

    def savePostData(self):
        try:
            self.postFetchedTime = datetime.now()
            self.post_last_updated_time = datetime.now()
            return mongo_connector.Mongo().save_data(collectionName='post', document=json.loads(self.json()))
        except Exception as e:
            logger.error(str(e))

    def findDataById(self, _id):
        try:
            found_data = mongo_connector.Mongo().find_data(_id)
            return found_data
        except Exception as e:
            logger.error(str(e))

    def update_all_post_details(self):

        query = {'$and': [{'registrationId': self.registrationId}, {'id': self.id}]}, self._preparePushData()

        return mongo_connector.Mongo().update(query)

    def _preparePushData(self):
        if self.data['mediaSource'] == 'faceBook':
            return {
                '$push': {'Object.faceBook.posts.data': {'id': self.Object['post_id'], 'createdTime': datetime.now(),
                                                         'message': self.Object['message']}}}
