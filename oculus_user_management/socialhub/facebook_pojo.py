from pydantic import BaseModel
from typing import Any, Optional






class FaceBook(BaseModel):
    app_id:str
    access_token:Optional[str]
    accounts:Optional[Any]
    business_users:Optional[Any]
    Object:Optional[Any]


    #Todo: CRUD opertaions
    def register_user(self):
        self.Object=self.__get_user_fields()
        return self.json()


    def __get_user_fields(self):
        return "id,name,accounts" \
            "{name,about,global_brand_page_name,access_token,category,connected_instagram_account," \
            "fan_count,features,followers_count,genre,has_whatsapp_business_number,instagram_business_account,business,tasks}," \
            "business_users{first_name,id,last_name,business,assigned_pages{name,global_brand_page_name,category,id,access_token,connected_instagram_account," \
            "followers_count,has_whatsapp_business_number,instagram_business_account,permitted_tasks,tasks}}"

