import os
from dotenv import load_dotenv
load_dotenv()
from pymongo import MongoClient

class Mongo:

    def __init__(self):
        self._client=MongoClient(os.environ.get('DATA_SOURCE_CONNECTION_STRING')).get_database('social')


    def save_data(self,collectionName,document):
        return self._client.get_collection(collectionName).insert_one(document).inserted_id




