import json
import time

from socialhub.oculusconnectorsapi import hub_Integration
from socialhub.facebook_pojo import FaceBook
from socialhub.twitter_pojo import Twitter
from socialhub.instagram_pojo import Instagram
from socialhub.linkedIn_pojo import LinkedIn
from google.protobuf.json_format import MessageToDict
from postmanagementdao import post_dao
from functools import wraps

from logs.studio_logger import Logger

logger = Logger("postManagementService")
from database.mongo_connector import Mongo

mongo_connector = Mongo()


def log_time(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        logger.info(f"Calling function: {func.__name__}")
        result = func(*args, **kwargs)
        elapsed_time = time.time() - start_time
        logger.info(f"Function {func.__name__} executed in {elapsed_time:.6f} seconds")
        return result

    return wrapper




class PostManagementService:

    @log_time
    def __save_data(self, social_hub_data, data):
        try:
            if not social_hub_data.get(data['mediaSource']).get('error'):
                _id = post_dao.UserPostDao(registrationId=data['registrationId'],
                                           pageId=data['registrationId'],
                                           Object=social_hub_data).savePostData()

                social_hub_data['status'] = _id
                logger.info(f"Data has been saved with id {_id}")
                # print('social_hub_data',social_hub_data)
                return social_hub_data
            else:
                error_message = f"An error occurred while creating post for user (user_id: {data['registrationId']}) on {data['mediaSource']}: " \
                                f"{social_hub_data.get(data['mediaSource']).get('error')}"
                raise Exception(error_message)
        except Exception as e:
            logger.error(str(e))

    def get_all_posts(self, data):
        try:
            logger.info(f"Request for get_all_posts() {data['registrationId']} received...")

            social_response = hub_Integration.getUserData(self.__prepare_get_all_posts_data(data))

            social_hub_data = MessageToDict(social_response)['responce']
            social_hub_data = json.loads(social_hub_data)

            return self.__save_data(social_hub_data, data)

        except Exception as e:
            logger.error(str(e))

    @log_time
    def create_post(self, data, scheduled=False, parent_id=None):
        try:
            if scheduled:
                mongo_job_id = data["_id"]
                mongo_connector.update('scheduler', mongo_job_id, 'success')

            logger.info(f"Request for create_post() for user (user_id: {data['registrationId']}) received...")
            hub_data = hub_Integration.postUserData(self.__prepare_data_for_create_post(data))
            social_hub_data = MessageToDict(hub_data).get('responce')
            social_hub_data = json.loads(social_hub_data)
            return self.__save_data(social_hub_data, data)

        except Exception as e:
            logger.error(str(e))
            if scheduled:
                mongo_job_id = data["_id"]
                mongo_connector.update('scheduler', mongo_job_id, f'Failed: {e}')







    @log_time
    def get_post(self, data):

        try:
            logger.info(f"Request for get_post() {data['registrationId']} received...")
            hub_data = hub_Integration.getUserData(self.__prepare_get_single_post_data(data))
            social_hub_data = json.loads(MessageToDict(hub_data)['responce'])
            return self.__save_data(social_hub_data, data)

        except Exception as e:
            logger.error(str(e))


    @log_time
    def __prepare_get_all_posts_data(self,data):

        logger.info("Preparing data for get_all_posts()...")
        try:
            processed_data = {
                'registrationId': data["registrationId"],
                'faceBook': {},
                'instagram': {},
                'twitter': {},
                'linkedIn': {}
            }

            if data['mediaSource'] == 'faceBook':
                processed_data['faceBook'] = FaceBook(appId=data['pageId'],
                                                      accessToken=data['accessToken']).getAllPostData()

            elif data['mediaSource'] == 'twitter':
                token_key = json.loads(data['accessToken'])
                processed_data['twitter'] = Twitter(bearerToken=token_key['bearerToken'], apiKey=token_key['apiKey'],
                                                    apiKeySecret=token_key['apiKeySecret'],
                                                    accessToken=token_key['accessToken'],
                                                    accessTokenSecret=token_key[
                                                        'accessTokenSecret']).prepare_get_all_posts_data()

            elif data['mediaSource'] == 'linkedIn':
                processed_data['linkedIn'] = LinkedIn(accessToken=data['accessToken'],
                                                      appId=data['pageId']).prepare_get_all_posts_data()

            json_string = json.dumps(processed_data)

            logger.info("Data for get_all_posts() prepared...")
            return json_string

        except Exception as e:
            logger.error(str(e))

    @log_time
    def __prepare_get_single_post_data(self,data):

        logger.info("Preparing data for get_single_post()...")

        try:
            processed_data = {
                'registrationId': data["registrationId"],
                'faceBook': {},
                'instagram': {},
                'twitter': {},
                'linkedIn': {}
            }

            if data['mediaSource'] == 'faceBook':
                processed_data['faceBook'] = FaceBook(appId=data['pageId'],
                                                      accessToken=data['accessToken']).getPostData()

            elif data['mediaSource'] == 'twitter':
                token_key = json.loads(data['accessToken'])
                processed_data['twitter'] = Twitter(bearerToken=token_key['bearerToken'], apiKey=token_key['apiKey'],
                                                    apiKeySecret=token_key['apiKeySecret'],
                                                    accessToken=token_key['accessToken'],
                                                    accessTokenSecret=token_key[
                                                        'accessTokenSecret']).prepare_get_single_post_data()

            elif data['mediaSource'] == 'linkedIn':
                processed_data['linkedIn'] = LinkedIn(appId=data['pageId'],
                                                      accessToken=data['accessToken']).prepare_get_single_post_data()

            json_string = json.dumps(processed_data)

            logger.info("Data for get_single_post() prepared...")

            return json_string

        except Exception as e:
            logger.error(str(e))

    @log_time
    def __prepare_data_for_create_post(self,data):

        logger.info("Preparing data for create_post()...")

        try:
            processed_data = {
                'registrationId': data["registrationId"],
                'twitter': {},
                'faceBook': {},
                'instagram': {},
                'linkedIn': {}
            }
            object_data = json.loads(data['Object'])
            if object_data['process'] == 'create':
                processed_data = self.create_post_data(data, processed_data, object_data['postData'])
            elif object_data['process'] == 'reshare':
                processed_data = self.reshare_post_data(data, processed_data, object_data['post_id'], object_data['message'])
            elif object_data['process'] == 'repost':
                if data['mediaSource'] == 'faceBook':
                    message, data = self.prepare_repost_data(data, object_data)
                processed_data = self.create_post_data(data, processed_data, message)

            json_string = json.dumps(processed_data)

            logger.info("Data for create_post() prepared...")

            return json_string

        except Exception as e:
            logger.error(str(e))

    def prepare_repost_data(self,data, object_data):
        data['pageId'] = object_data['post_id']
        post_data = PostManagementService().get_post(data)
        message = post_data[data['mediaSource']]['message']
        data['pageId'] = post_data[data['mediaSource']]['id'].split('_')[0]

        return message, data

    def create_post_data(self,data, processed_data, message):
        try:
            if data['mediaSource'] == 'faceBook':
                processed_data['faceBook'] = FaceBook(appId=data['pageId'],
                                                      accessToken=data['accessToken']).createPostData(message)


            elif data['mediaSource'] == 'twitter':
                token_key = json.loads(data['accessToken'])
                processed_data['twitter'] = Twitter(bearerToken=token_key['bearerToken'], apiKey=token_key['apiKey'],
                                                    apiKeySecret=token_key['apiKeySecret'],
                                                    accessToken=token_key['accessToken'],
                                                    accessTokenSecret=token_key['accessTokenSecret']).create_post_data(
                    message)

            elif data['mediaSource'] == 'linkedIn':
                processed_data['linkedIn'] = LinkedIn(accessToken=data['accessToken'],
                                                      appId=data['pageId']).create_post_data(message)
            return processed_data
        except Exception as e:
            logger.error(str(e))

    def reshare_post_data(self,data, processed_data, post_id, message=None):
        try:
            if data['mediaSource'] == 'faceBook':
                processed_data['faceBook'] = FaceBook(appId=data['pageId'],
                                                      accessToken=data['accessToken']).sharePostData(post_id)


            elif data['mediaSource'] == 'twitter':

                token_key = json.loads(data['accessToken'])
                processed_data['twitter'] = Twitter(bearerToken=token_key['bearerToken'], apiKey=token_key['apiKey'],
                                                    apiKeySecret=token_key['apiKeySecret'],
                                                    accessToken=token_key['accessToken'],
                                                    accessTokenSecret=token_key['accessTokenSecret']).create_post_data(
                    message)

            elif data['mediaSource'] == 'linkedIn':
                processed_data['linkedIn'] = LinkedIn(accessToken=data['accessToken'],
                                                      appId=data['pageId']).sharePostData(post_id, message)
            return processed_data
        except Exception as e:
            logger.error(str(e))


