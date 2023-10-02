import requests


if __name__ == '__main__':

    page_id = "103658366092003"
    page_access_token = "EAAathGdn1gcBOZBoQCq8Cogy4YUBSjT7iKqZAyQW7nTxJUmVX2zgskd16ZCwsVyN3HQZCuKuYvog7SBRPJHMflgZCrkIJA4VXL2d7At7VTRuRVIFGqBzS7H3Cg5JsS1fveYZAhtDK41O0lQfphiGJqyy8hAO7kR1rI2sea3hAenLx3ZBzJZC9WD95DDR2JyiBXfxtOd7kqQZD"
    image_path = "/home/sumit/Desktop/postManagementService/DataNext/src/python/social/socialHubIntegrationService/multimedia/image.jpg"
    message = "This is awesome as well..."

    with open(image_path, "rb") as file:
        url = f"https://graph.facebook.com/v17.0/{page_id}/photos"

        headers = {
            "Authorization": f"Bearer {page_access_token}"
        }

        files = {
            "source": ("test_image", file, "image/jpeg")
        }

        data = {
            "message": message
        }

        response = requests.post(url, headers=headers, files=files, data=data)

        print(response.status_code)

        print(response.text)
