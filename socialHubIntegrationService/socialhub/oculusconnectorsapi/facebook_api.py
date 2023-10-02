import json

from pydantic import BaseModel
from typing import Any, Optional
from pyfacebook import GraphAPI

from logs.studio_logger import Logger
logger = Logger("socialHubIntegrationService")


class Facebook_graph_api(BaseModel):
    access_token: Optional[str]
    app_id: Optional[str]
    Object: Optional[str]

    def getUserData(self):
        try:

            response = GraphAPI(access_token=self.access_token).get_object(object_id=self.app_id,
                                                                           fields=self.Object)
            logger.info("Received successful response from get_user_data call to Facebook GraphAPI...")
            return response

        except Exception as e:
            error = f"An Exception occurred while making get_user_data call to Facebook GraphAPI: {e}"
            logger.info(error)
            return {"error": str(e)}

    def postUserData(self):
        try:
            self.Object = json.loads(self.Object)
            response = GraphAPI(access_token=self.access_token).post_object(object_id=self.app_id,
                                                                            connection=self.Object['connection'],
                                                                            params={'message': self.Object['message']})
            logger.info("Received successful response from post_data call to Facebook GraphAPI...")
            return response

        except Exception as e:
            error = f"An Exception occurred while making post_data call to Facebook GraphAPI: {e}"
            logger.info(error)
            return {"error": str(e)}

    def deleteUserData(self):
        try:
            return GraphAPI(access_token=self.access_token). \
                delete_object(object_id=self.app_id, fields=self.Object)

        except Exception as e:
            error = f"An Exception occurred while making delete_post call to Facebook GraphAPI: {e}"
            logger.info(error)
            return {"error": str(e)}

    # Todo:Do something for fields

    # def __get_user_fields(self):
    #     return "id,name,accounts" \
    #            "{name,about,global_brand_page_name,access_token,category,connected_instagram_account," \
    #            "fan_count,features,followers_count,genre,has_whatsapp_business_number,instagram_business_account,business,tasks}," \
    #            "business_users{first_name,id,last_name,business,assigned_pages{name,global_brand_page_name,category,id,access_token,connected_instagram_account," \
    #            "followers_count,has_whatsapp_business_number,instagram_business_account,permitted_tasks,tasks}}"