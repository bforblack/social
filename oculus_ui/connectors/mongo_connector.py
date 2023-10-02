import os
from logs.logger import Logger
import pymongo
from bson import ObjectId

logger = Logger()


class MONGODB:
    def __init__(self):
        # database socket
        myclient = pymongo.MongoClient(os.getenv("MONGO_CRED"))
        mydb = myclient["mydatabase"]
        self.mycol = mydb["social"]

    def data_add(self, mydict):
        """
        :param mydict: input dictionary
        :return: object id
        """
        try:
            objInstance = self.mycol.insert_one(mydict)
            return objInstance
        except Exception as e:
            logger.error_msg(f'adding data in mongo got failed {e}')

    def data_update(self, data_id, data):
        """
        :param data_id: mongo update object id
        :param data: updatable dictionary
        :return: -
        """
        try:

            self.mycol.update_many({"_id": data_id}, {'$set': data})
        except Exception as e:
            logger.error_msg(f'data update in mongo got failed {e}')

    def read_data(self, id):
        """
        :param id: mongo object id
        :return: dictionary data
        """
        try:
            predicted_data = self.mycol.find_one(ObjectId(id))
            return predicted_data
        except Exception as e:
            logger.error_msg(f'mongo reading failed {e}')
