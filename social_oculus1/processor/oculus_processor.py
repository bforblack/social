from oculus_source import source_connector





def getuserdata(user_id):
     source_connector.get_data_base_connector().get_database('social').get_collection('user').find({"_id":user_id})

def saveuserdata(data):
     source_connector.get_data_base_connector().get_database('social').get_collection('user').insert_one(document=data)



