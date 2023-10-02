from pydantic import BaseModel
from typing import Any, Optional
from socialhub.oculusconnectorsapi import facebook_api

from logs.studio_logger import Logger
logger = Logger("socialHubIntegrationService")


class FaceBook(BaseModel):
    appId: Optional[str]
    accessToken: Optional[str]
    accounts: Optional[Any]
    businessUsers: Optional[Any]
    Object: Optional[str]

    def getUserData(self):

        try:

            empty_fields = [field_name for field_name in ["appId", "accessToken", "Object"]
                            if not getattr(self, field_name) or getattr(self, field_name, '').strip() == '']

            if len(empty_fields) == 3:
                return {}

            elif empty_fields:
                error = f"The following fields cannot be empty: {', '.join(empty_fields)}"
                logger.info(f"An exception occurred while registering Facebook user: {error}")
                error_message = {"error": error}
                return error_message

            else:
                response = facebook_api.Facebook_graph_api(app_id=self.appId, access_token=self.accessToken,
                                                           Object=self.Object).getUserData()
                return response

        except Exception as e:
            error = f"An exception occurred while registering Facebook user: {e}"
            logger.info(error)
            error_message = {"error": error}
            return error_message

    def postUserData(self):

        try:

            empty_fields = [field_name for field_name in ["appId", "accessToken", "Object"]
                            if not getattr(self, field_name) or getattr(self, field_name, '').strip() == '']

            if len(empty_fields) == 3:
                return {}

            elif empty_fields:
                error = f"The following fields cannot be empty: {', '.join(empty_fields)}"
                logger.info(f"An exception occurred while posting data on Facebook: {error}")
                error_message = {"error": error}
                return error_message

            else:
                response = facebook_api.Facebook_graph_api(app_id=self.appId, access_token=self.accessToken,
                                                           Object=self.Object).postUserData()
                return response

        except Exception as e:
            error = f"An exception occurred while posting data on Facebook: {e}"
            logger.info(error)
            error_message = {"error": error}
            return error_message
