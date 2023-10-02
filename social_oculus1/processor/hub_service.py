from pyfacebook import GraphAPI
from processor import oculus_processor as oc







def getUserData(access_token,app_id):
    data=GraphAPI(access_token=access_token,app_id=app_id).get_object(object_id=app_id,fields='id,name,accounts{about,access_token,'
                                                                                              'connected_instagram_account,business,category_list,instagram_business_account}')
    oc.saveuserdata(data)
    return True