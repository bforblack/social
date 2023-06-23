from oculusdao import oculus_user_dao
from socialhub.oculusconnectorsapi import hub_Integration

class UserService:

#Todo: implement Other methods
    def registerUser(self,data):
       return oculus_user_dao.User(**hub_Integration.getUserData(data)).register()

    def getUser(self,userID):
        pass

    def updateUser(self):
        pass

    def removeUser(self):
        pass