from pydantic import BaseModel
from oculus_api import linkedin_api


class Linkedin(BaseModel):
    app_id:str
    access_token:str


    def register_user(self):
        return linkedin_api.Linkedin_graph_api( access_token=self.access_token,
        app_id=self.app_id).get_user()