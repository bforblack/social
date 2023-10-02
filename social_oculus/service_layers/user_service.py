from database import mongo_connector
from service import user_management


class UserService:

    def __init__(self):
        self.connection = mongo_connector.Mongo('user')

    def register(self, data):
        return user_management.registerUser(data).registrationId

    def getUserDataById(self, regestrationId):
        return self.connection.find_one({"registrationId": regestrationId})

    # Query to get data auth data if  for particualr id

    def getPageAuthDetails(self, registrationId, mediaSource, pageId):
        # mediaSourceDetails = {'faceBook': '[faceBook][accounts][data]','linkedIn':'fill_your_values'}
        mediaSourceDetailsAuthKeys = {'faceBook': 'access_token', 'linkedIn': 'accessToken'}
        userData = self.connection.find({'registrationId': registrationId})
        if mediaSource == 'faceBook':
            data = userData['faceBook']['accounts']['data']
            for d in data:
                if d['id'] == pageId:
                    authKey = d[mediaSourceDetailsAuthKeys[mediaSource]]
                    pass
        elif mediaSource == 'linkedIn':
            authKey = userData['linkedIn']['accessToken']
            print(authKey)
            pass

        return authKey
