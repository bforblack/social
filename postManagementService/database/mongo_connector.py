import os
from dotenv import load_dotenv
load_dotenv()
from pymongo import MongoClient

class Mongo:

    def __init__(self):
        self._client=MongoClient(os.environ.get('DATA_SOURCE_CONNECTION_STRING')).get_database('social')

    def save_data(self,collectionName, document):
        return self._client.get_collection(collectionName).insert_one(document).acknowledged

    def find_data(self,collectionName,document):
        return self._client.get_collection(collectionName).find_one(document)
    def find_all(self, collectionName):
        return self._client.get_collection(collectionName).find()

    def update(self, collectionName, mongo_job_id, status):
        # The criteria to find the document you want to update (e.g., a unique identifier)
        filter_criteria = {"_id": mongo_job_id}

        # The update operation using $set to update the specific column
        update_operation = {"$set": {"status": status}}

        # Update the document

        return self._client.get_collection(collectionName).update_one(filter_criteria, update_operation)



