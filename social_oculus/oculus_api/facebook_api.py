from pydantic import BaseModel
from typing import Any,Optional
from pyfacebook import GraphAPI

class Facebook_graph_api(BaseModel):
    access_token:Any
    app_id:Any
    Object:Optional[Any]




    def getUserData(self):
        return GraphAPI(access_token=self.access_token).\
            get_object(object_id=self.app_id,fields=self.__get_user_fields())

    def post_data(self,message):
       return GraphAPI(access_token=self.access_token).post_object(object_id=self.app_id,connection='feed',params={'messsage':message})

    def removePost(self, id):
        return GraphAPI(access_token=self.access_token).delete_object(id)

    def getAllPostdetails(self,nodeData):
        if(self.nodeData!=None):
            return GraphAPI(access_token=self.access_token).get_object(id=self.app_id, fields='post&'+nodeData)
        else:
            return GraphAPI(access_token=self.access_token).get_object(id=self.app_id, fields='post')


    def getPostDetailsById(self):
        return GraphAPI(access_token=self.access_token).get_object(id=self.app_id,fields=self.__get_post_fields())

    #Todo: generaic method to get data using node
    def getnodeData(self,nodeData):
        pass
        #return GraphAPI(access_token=self.access_token).get_object(id=self.app_id, fields=self.__get_post_fields())



    # def getPostDetailsById(self):
    #     return GraphAPI(access_token=self.access_token).get_object(id=self.app_id, fields='post')






    #Todo:Do something for fields

    def __get_user_fields(self):
        return "id,name,accounts" \
               "{name,about,global_brand_page_name,access_token,category,connected_instagram_account," \
               "fan_count,features,followers_count,genre,has_whatsapp_business_number,instagram_business_account,business,tasks}," \
               "business_users{first_name,id,last_name,business,assigned_pages{name,global_brand_page_name,category,id,access_token,connected_instagram_account," \
               "followers_count,has_whatsapp_business_number,instagram_business_account,permitted_tasks,tasks}}"

    def __get_post_fields(self):
        return 'message,created_time,likes{id,username,name,pic_square},comments{from,id,user_likes,reactions' \
               '{id,name,username,pic_small,type},message,like_count,comment_count,likes{id,name,username}},' \
               'instagram_eligibility,shares,message_tags,subscribed,' \
               'sharedposts,is_popular,timeline_visibility,admin_creator,feed_targeting,updated_time'

