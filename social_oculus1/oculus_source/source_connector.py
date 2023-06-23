import os
from dotenv import load_dotenv
load_dotenv()
from pymongo import MongoClient
import motor.motor_asyncio

def get_data_base_connector():
    return _monogo_connector()


def _monogo_connector()->MongoClient:
    return MongoClient(os.environ.get('DATA_SOURCE_CONNECTION_STRING'))
    # client = motor.motor_asyncio.AsyncIOMotorClient(os.environ.get('DATA_SOURCE_CONNECTION_STRING'))
    # database = client.social
    # return database.get_collection("social")




