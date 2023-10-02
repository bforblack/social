from database import mongo_connector
from service import post_management
class PostService():

    def get_all_post_Of_page(self,registrationId,pageId):
        #queryParam=list.append(registrationId=registrationId,pageId=pageId)
        query={'$and':[{'registrationId':registrationId},{'id':pageId}]}
        return mongo_connector.Mongo('post').find(query)
        #Todo: for other connctors





    def get_page_data_from_hub(self,registrationId,mediaSource,authData,pageId):
        return post_management.getAllPost(mediaSource=mediaSource, pageId=pageId,
                                         accessToken=authData,registrationId=registrationId)



    def get_post_details_from_hub(self,registrationId,mediaSource,postId,authData):
        return post_management.getPostedDataDetails(mediaSource=mediaSource, pageId=postId,
                                          accessToken=authData, registrationId=registrationId)


    def createPost(self,registrationId,mediaSource,authData,pageId,postData):
        return post_management.createPost(registrationId,mediaSource,authData,pageId,postData)


