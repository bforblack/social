import json

from pydantic import BaseModel
from typing import Any, Optional

from socialhub.oculusconnectorsapi.linkedin_api import LinkedInAPI

from logs.studio_logger import Logger
logger = Logger("socialHubIntegrationService")


class LinkedIn(BaseModel):
    appId: Optional[str]
    accessToken: Optional[str]
    Object: Optional[str]

    # def get_user_data(self):
    #     empty_fields = [field_name for field_name in ["accessToken", "Object"]
    #                     if not getattr(self, field_name) or getattr(self, field_name, '').strip() == '']
    #
    #     if len(empty_fields) == 2:
    #         return {}
    #
    #     elif empty_fields:
    #         error = f"The following fields cannot be empty: {', '.join(empty_fields)}"
    #         logger.info(f"An exception occurred while registering LinkedIn user: {error}")
    #         error_message = {"error": error}
    #         return error_message
    #
    #     else:
    #         _object = json.loads(self.Object)
    #         service = _object.get('service')
    #
    #         if service == 'oculus_user_management':
    #             url = _object.get('url')
    #             response = LinkedInAPI(accessToken=self.accessToken).get_user_data(url=url)
    #             return response
    #
    #         elif service == 'oculus_post_management':
    #             url = _object.get('url')
    #             payload = _object.get('payload')
    #             author = payload.get('author')
    #             response = LinkedInAPI(accessToken=self.accessToken).get_posts(url=url,
    #                                                                            author=author)
    #             return response

    def get_user_data(self):
        try:
            empty_fields = [field_name for field_name in ["accessToken", "Object"]
                            if not getattr(self, field_name) or getattr(self, field_name, '').strip() == '']

            if len(empty_fields) == 2:
                return {}

            elif empty_fields:
                error = f"The following fields cannot be empty: {', '.join(empty_fields)}"
                logger.info(f"An exception occurred while registering LinkedIn user: {error}")
                error_message = {"error": error}
                return error_message

            else:
                _object = json.loads(self.Object)
                url = _object.get('url')
                response = LinkedInAPI(accessToken=self.accessToken).get_user_data(url=url)
                response['pageId'] = self.appId

                return response

        except Exception as e:
            logger.info(f"An exception occurred while registering LinkedIn user: {str(e)}")
            error_message = {"error": str(e)}
            return error_message

    def post_data(self):
        empty_fields = [field_name for field_name in ["accessToken", "Object"]
                        if not getattr(self, field_name) or getattr(self, field_name, '').strip() == '']

        if len(empty_fields) == 2:
            return {}

        elif empty_fields:
            error = f"The following fields cannot be empty: {', '.join(empty_fields)}"
            logger.info(f"An exception occurred while registering LinkedIn user: {error}")
            error_message = {"error": error}
            return error_message

        else:
            try:
                _object = json.loads(self.Object)
                url = _object.get('url')
                payload = _object.get('payload')
                author = payload.get('author')
                post = payload.get('post')
                response = LinkedInAPI(accessToken=self.accessToken).post_data(url=url,
                                                                               author=author,
                                                                               post=post)
                return response

            except Exception as e:
                logger.info(f"An exception occurred while posting data on LinkedIn: {str(e)}")
                error_message = {"error": str(e)}
                return error_message

    def get_posts(self):
        empty_fields = [field_name for field_name in ["accessToken", "Object"]
                        if not getattr(self, field_name) or getattr(self, field_name, '').strip() == '']

        if len(empty_fields) == 2:
            return {}

        elif empty_fields:
            error = f"The following fields cannot be empty: {', '.join(empty_fields)}"
            logger.info(f"An exception occurred while registering LinkedIn user: {error}")
            error_message = {"error": error}
            return error_message

        else:
            try:
                _object = json.loads(self.Object)
                url = _object.get('url')
                payload = _object.get('payload')
                author = payload.get('author')
                response = LinkedInAPI(accessToken=self.accessToken).get_posts(url=url,
                                                                               author=author)
                return response

            except Exception as e:
                logger.info(f"An exception occurred while posting data on LinkedIn: {e}")
                error_message = {"error": e}
                return error_message
