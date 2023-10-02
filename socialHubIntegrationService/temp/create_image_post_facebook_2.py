import requests
import base64
from io import BytesIO


def post_image_data(url, page_access_token, post, base64_image_data):

    decoded_image_data = base64.b64decode(base64_image_data)

    image_file = BytesIO(decoded_image_data)

    headers = {
        "Authorization": f"Bearer {page_access_token}"
    }

    files = {
        "source": ("image.jpg", image_file)
    }

    data = {
        "message": post
    }

    response = requests.post(url, headers=headers, files=files, data=data)

    if response.status_code == 200:
        print("Image posted successfully on Facebook...")

    else:
        print("Image post on Facebook failed...")

    return response.json()


if __name__ == '__main__':

    page_id = "103658366092003"
    _url = f"https://graph.facebook.com/v17.0/{page_id}/photos"

    _page_access_token = "EAAathGdn1gcBOZBoQCq8Cogy4YUBSjT7iKqZAyQW7nTxJUmVX2zgskd16ZCwsVyN3HQZCuKuYvog7SBRPJHMflgZCrkIJA4VXL2d7At7VTRuRVIFGqBzS7H3Cg5JsS1fveYZAhtDK41O0lQfphiGJqyy8hAO7kR1rI2sea3hAenLx3ZBzJZC9WD95DDR2JyiBXfxtOd7kqQZD"

    _post = "This is a beautiful image 001..."

    _image_file_path = "../multimedia/image.jpg"

    with open(_image_file_path, "rb") as file:
        _base64_image_data = base64.b64encode(file.read()).decode()

    posted = post_image_data(_url, _page_access_token, _post, _base64_image_data)

    print(posted)
