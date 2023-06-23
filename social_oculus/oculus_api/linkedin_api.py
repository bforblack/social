from pydantic import BaseModel
from typing import Any
from linkedin import linkedin

class Linkedin_graph_api(BaseModel):
    access_token: Any
    app_id: Any


    def get_user(self):
        auth=linkedin.LinkedInDeveloperAuthentication\
            (consumer_key=self.app_id,consumer_secret=self.access_token)

        return linkedin.LinkedInApplication().make_request(params='/me')
