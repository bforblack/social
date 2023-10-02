
from pydantic import BaseModel



class FaceBook(BaseModel):
    appId:str
    accessToken:str

class Instagram(BaseModel):
    appId: str
    accessToken: str


class Twitter(BaseModel):
    bearerToken: str
    apiKey: str
    apiKeySecret: str
    accessToken: str
    accessTokenSecret:str

class LinkedIn(BaseModel):
    appId:str
    accessToken:str
    # def register_user(self):
    #     return facebook_api.Facebook_graph_api(app_id=self.app_id, access_token=self.access_token).getUserData()
    #
    # def post_data(self,message):
    #     for x in self.accounts['data']:
    #                         if x['id']==self.app_id:
    #                             self.access_token= x['access_token']
    #
    #     return facebook_api.Facebook_graph_api(app_id=self.app_id, access_token=self.access_token).post_data(message)
    #
    # def delete(self,id):
    #     return facebook_api.Facebook_graph_api(app_id=self.app_id, access_token=self.access_token).removePost(id)
    #
    # def getposts(self):
    #     return facebook_api.Facebook_graph_api(app_id=self.app_id, access_token=self.access_token).getallFaceBookPost()
    #
    #
    # def getpostData(self,id):
    #     return facebook_api.Facebook_graph_api(app_id=self.app_id, access_token=self.access_token).getallFaceBookPost()

















