import requests
import base64
from io import BytesIO

from logs.studio_logger import Logger
logger = Logger("socialHubIntegrationService")


def post_image_data(url, access_token, post, base64_image_data):

    logger.info("Creating facebook image post...")

    try:
        decoded_image_data = base64.b64decode(base64_image_data)

        image_file = BytesIO(decoded_image_data)

        headers = {
            "Authorization": f"Bearer {access_token}"
        }

        files = {
            "source": ("image.jpg", image_file)
        }

        data = {
            "message": post
        }

        response = requests.post(url, headers=headers, files=files, data=data)

        if response.status_code == 200:
            logger.info("Facebook image post successfully created...")
            return response.json()

        else:
            error_message = f"Image post on Facebook failed: {response.text}"
            logger.info(error_message)
            error = {"error": error_message}
            return error

    except Exception as e:
        error_message = f"Image post on facebook failed: {str(e)}"
        logger.info(error_message)
        error = {"error": error_message}
        return error


if __name__ == '__main__':

    page_id = "103658366092003"
    _url = f"https://graph.facebook.com/v17.0/{page_id}/photos"

    _page_access_token = "EAAathGdn1gcBOZBoQCq8Cogy4YUBSjT7iKqZAyQW7nTxJUmVX2zgskd16ZCwsVyN3HQZCuKuYvog7SBRPJHMflgZCrkIJA4VXL2d7At7VTRuRVIFGqBzS7H3Cg5JsS1fveYZAhtDK41O0lQfphiGJqyy8hAO7kR1rI2sea3hAenLx3ZBzJZC9WD95DDR2JyiBXfxtOd7kqQZD"

    _post = "This is a beautiful image 001..."

    _image_file_path = "/home/sumit/Desktop/postManagementService/DataNext/src/python/social/socialHubIntegrationService/multimedia/image.jpg"

    with open(_image_file_path, "rb") as file:
        _base64_image_data = base64.b64encode(file.read()).decode()

    posted = post_image_data(_url, _page_access_token, _post, _base64_image_data)

    print(posted)
