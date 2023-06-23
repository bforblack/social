from pydantic import BaseModel
from typing import Any,Optional
from pyfacebook import GraphAPI

class Facebook_graph_api(BaseModel):
    access_token:Any
    app_id:Any
    Object:Optional[Any]




    def getCommentsRelatedData(self):
        return GraphAPI(access_token=self.access_token).\
            get_object(object_id=self.app_id,fields=self.__getCommentsRelatedFields())
    GraphAPI().get()




    #Todo:Do something for fields

    def __getCommentsRelatedFields(self):
        return 'comments{from,id,message,like_count,user_likes,comment_count,reactions{id,name,pic_small,username},' \
               'created_time,likes{id,name,pic_small}},likes{id,name,pic_small,username}'




if __name__ == '__main__':
    data={"access_token":"110928107339307","access_token":"EAADp0kuQjd0BAEz27iN1n0SQBLgTj7aOsGZBTjQpgMZBDRjmbiWy2UpmZANZChMfcJ6vCZBmYUTUKZBLZCPuj7WauJ9d0RaW96Im9gWQgqe65r8nh8vm9oCLod2NislpScnN8cUttHjYexA34lOZBeQXAAXiavHQIwninETYkLO62MWyGBkk7rqhLL0TSHUTZBlWKrS4nMCXZB51L7STDgWlIi"}
    Facebook_graph_api(**data).getCommentsRelatedData()


