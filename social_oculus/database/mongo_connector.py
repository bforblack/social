import os
from dotenv import load_dotenv
load_dotenv()
from pymongo import MongoClient

class Mongo:

    def __init__(self,collectionName):
        self._client=MongoClient(os.environ.get('DATA_SOURCE_CONNECTION_STRING')).get_database('social').get_collection(collectionName)


    def save_data(self,collectionName,document):
       return self._client.get_collection(collectionName).insert_one(document).acknowledged

    def find_one(self,document):
        # print()
       return self._client.find_one(document,{'_id':0})

    def save_data_user(self,document):
        return self._client.insert_one(document).acknowledged

    def find(self, query):
        return self._client.find_one(query, {'_id': 0})


    # def  find_one(self,collectionName,document):
    #     return self._client.get_collection(collectionName).find_one(document,{'_id':0})

    # def find(self):
    #     return self._client.get_collection('user').find_one({"$and":[{'registrationId':'c3b6c077-d57b-4f94-8023-aad251d351b5'},{'110928107339307':
    # {'$exists':1}}]})


if __name__ == '__main__':
    Mongo().check()