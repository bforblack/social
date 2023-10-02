import os
from dotenv import load_dotenv
load_dotenv()
from pymongo import MongoClient

from logs.studio_logger import Logger
logger = Logger("oculusUserManagement")


class Mongo:

    def __init__(self):
        self._client = MongoClient(os.environ.get('DATA_SOURCE_CONNECTION_STRING')).get_database('social').get_collection('user')


    def save_data(self, collectionName, document):
        try:
            return self._client.insert_one(document).acknowledged
        except Exception as e:
            logger.error(str(e))

    def update_one(self,id,document):
        return self._client.update_one({'registrationId':id},{'$set':document},upsert=False).acknowledged




