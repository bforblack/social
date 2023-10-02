from bson.objectid import  ObjectId
from pydantic import BaseModel,Field,Json
from typing import Optional,Any

from social_hub import connectors
import json
from service import post_management
from google.protobuf.json_format import MessageToDict
from service import analytics
from database import mongo_connector
from service_layers import post_service,user_service




class Oculus(BaseModel):
    username:Optional[str]
    registrationId:Optional[str]
    faceBook:Optional[connectors.FaceBook]
    twitter:Optional[connectors.Twitter]
    linkedIn:Optional[connectors.LinkedIn]
    instagram:Optional[connectors.Instagram]


    def registerUser(self):
        return user_service.UserService().register(json.loads(self.json(exclude={'registrationId'})))


    def getUserById(self,id):
        return user_service.UserService().getUserDataById(id)



    def getpostDetails(self,id,mediaSource,postId=None,pageId=None):
        if postId is not None:
            return self.__get_post_related_data(
                registrationId=id, postId=postId, mediaSource=mediaSource)
        else:
            return self.__get_page_related_data \
                (registrationId=id, pageId=pageId, mediaSource=mediaSource)



    def __get_page_related_data(self, registrationId,pageId,mediaSource):
        postData = post_service.PostService().get_all_post_Of_page(registrationId=registrationId, pageId=pageId)
        if postData is not None:
            return self.__retrieveData_as_per_mediaType(postData, mediaSource=mediaSource)
        else:
            authData = user_service.UserService().getPageAuthDetails(registrationId=registrationId, mediaSource=mediaSource,pageId=pageId)

            # print(registrationId,mediaSource,authData,pageId)
            postData = MessageToDict(
                post_service.PostService().get_page_data_from_hub(registrationId=registrationId, mediaSource=mediaSource,
                                                                  authData=authData,pageId=pageId))
            postData['postList'] = json.loads(postData['postList'])
            return self.__retrieveData_as_per_mediaType(postData['postList'], mediaSource=mediaSource)





    def __get_post_related_data(self,registrationId,postId,mediaSource):
        postData = post_service.PostService().get_all_post_Of_page(registrationId=registrationId, pageId=postId)

        if postData is not None:
            return postData
        else:

            authData = user_service.UserService().getPageAuthDetails(registrationId=registrationId,
                                                                     mediaSource=mediaSource, pageId=self.__get_pageid_from_postId(postId))
            postData = MessageToDict(
                post_service.PostService().get_post_details_from_hub(registrationId=registrationId, mediaSource=mediaSource,
                                                                  authData=authData,postId=postId))
            postData['postList'] = json.loads(postData['postList'])
            return self.__retrieveData_as_per_mediaType(postData['postList'], mediaSource=mediaSource)




    def __get_pageid_from_postId(self,postId):
        spl_char = "_"
        last_index = postId.rfind(spl_char)
        pageId = postId[:last_index]
        return pageId



    def __retrieveData_as_per_mediaType(self, postData, mediaSource):
            # Todo: for other source connectors as par data saved or simplyfy this as genric fetch for all
            if mediaSource == 'faceBook':
                # print(postData)
                return postData['faceBook']







    def createPost(self,id,mediaSource,pageId,data):
        authData=user_service.UserService().getPageAuthDetails(registrationId=id,
                                                            mediaSource=mediaSource, pageId=pageId)

        return MessageToDict(post_service.PostService().createPost(registrationId=id,mediaSource=mediaSource,authData=authData,pageId=pageId,postData=data))['postId']





