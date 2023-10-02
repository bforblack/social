import requests
import json
from pydantic import BaseModel
from typing import Any, Optional

from logs.studio_logger import Logger
logger = Logger("socialHubIntegrationService")


class LinkedInAPI(BaseModel):
    appId: Optional[str]
    accessToken: Optional[str]
    Object: Optional[Any]

    def get_user_data(self, url):

        try:
            headers = {
                'Authorization': f'Bearer {self.accessToken}'
            }

            response = requests.request("GET", url, headers=headers)

            if response.status_code == 200:
                logger.info("Received successful response from get_user_data() call to LinkedIn API...")
                data = response.json()
                data['accessToken'] = self.accessToken
                data['pageId'] = self.appId
                return data
            else:
                logger.info(f"Received negative response from LinkedIn while making get_user_data call to LinkedIn API: {response.text}")
                return {"error": response.text}

        except Exception as e:
            logger.info(f"An Exception occurred while making get_user_data() call to LinkedIn API: {str(e)}")
            return {"error": str(e)}

    def post_data(self, url, author, post):

        try:
            payload = json.dumps({
                "author": author,
                "commentary": post,
                "visibility": "PUBLIC",
                "distribution": {
                    "feedDistribution": "MAIN_FEED",
                    "targetEntities": [],
                    "thirdPartyDistributionChannels": []
                },
                "lifecycleState": "PUBLISHED",
                "isReshareDisabledByAuthor": False
            })

            headers = {
                'Content-Type': 'application/json',
                'Authorization': f'Bearer {self.accessToken}',
            }

            response = requests.post(url, headers=headers, data=payload)

            if response.status_code == 201:
                logger.info("Received successful response from post_data call to Linkedin API...")
                post_id = response.headers.get('x-linkedin-id')
                post_data = {'post_status': 'success', 'post_id': post_id}
                return post_data
            else:
                logger.info(f"Received negative response from LinkedIn while making post_data call to LinkedIn API: {response.text}")
                return {"error": response.text}

        except Exception as e:
            logger.info(f"An Exception occurred while making post_data() call to LinkedIn API: {str(e)}")
            return {"error": str(e)}

    def get_posts(self, url, author):
        total_posts = []

        try:
            start = 0
            count = 10
            next_page = True
            while next_page:

                _url = url + f"?q=author&author={author}&start={start}&count={count}"

                headers = {
                    'Content-Type': 'application/json',
                    'Authorization': f'Bearer {self.accessToken}',
                }
                response = requests.get(_url, headers=headers)

                if response.status_code == 200:
                    data = response.json()
                    posts = data.get('elements')
                    total_posts = total_posts + posts
                    posts_count = data.get('paging').get('total')

                else:
                    logger.info(f"Received negative response from LinkedIn while making post_data() call to LinkedIn API: {response.text}")
                    return {"posts": total_posts, "error": response.text}

                start = start + 10

                if posts_count <= start:
                    next_page = False
                    logger.info("Received successful response from get_posts() call to Linkedin API...")
                    return {"posts": total_posts}

        except Exception as e:
            logger.info(f"An Exception occurred while making post_data() call to LinkedIn API: {str(e)}")
            return {"error": str(e)}
