import os
from dotenv import load_dotenv
load_dotenv()
from pymongo import MongoClient
import motor.motor_asyncio
from minio import Minio

def get_data_base_connector():
    return _monogo_connector()


def _monogo_connector()->MongoClient:
    return MongoClient(os.environ.get('DATA_SOURCE_CONNECTION_STRING'))
    # client = motor.motor_asyncio.AsyncIOMotorClient(os.environ.get('DATA_SOURCE_CONNECTION_STRING'))
    # database = client.social
    # return database.get_collection("social")

def _minio_connector()->Minio:
    return  Minio(endpoint=os.environ.get('MINIO_END_POINT'),secure=False,
                  access_key=os.environ.get('MINIO_ACCESS_KEY'),
                 secret_key=os.environ.get('MINIO_SECERET_KEY'))

