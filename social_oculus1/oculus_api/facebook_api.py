from pydantic import BaseModel
from typing import Any
from pyfacebook import GraphAPI

class Facebook_graph_api(BaseModel):
    access_token:Any
    app_id:Any



    def getUserData(self):
        return GraphAPI(access_token=self.access_token).\
            get_object(object_id=self.app_id,fields=self.__get_user_fields())

    def post_data(self,message):
       return GraphAPI(access_token=self.access_token).post_object(object_id=self.app_id,connection='feed',params={'messsage':message})


    def removePost(self, id):
        return GraphAPI(access_token=self.access_token).delete_object(id)


#Todo:Do something for fields

    def __get_user_fields(self):
        return "id,name,accounts" \
               "{name,about,global_brand_page_name,access_token,category,connected_instagram_account," \
               "fan_count,features,followers_count,genre,has_whatsapp_business_number,instagram_business_account,business,tasks}," \
               "business_users{first_name,id,last_name,business,assigned_pages{name,global_brand_page_name,category,id,access_token,connected_instagram_account," \
               "followers_count,has_whatsapp_business_number,instagram_business_account,permitted_tasks,tasks}}"


