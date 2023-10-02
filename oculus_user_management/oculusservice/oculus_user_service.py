from oculusdao import oculus_user_dao
from socialhub.oculusconnectorsapi import hub_Integration
import json

from logs.studio_logger import Logger
logger = Logger("oculusUserManagement")


class UserService:

#Todo: implement Other methods
    def registerUser(self,data):
       return oculus_user_dao.User(**data).register()
       # data1=hub_Integration.getUserData(copy.deepcopy(data).pop('lastUpatedTime'))
       # return oculus_user_dao.User(**json.loads(data1.responce)).register()

    def getUser(self,userID):
        pass

    def updateUser(self):
        pass

    def removeUser(self):
        pass