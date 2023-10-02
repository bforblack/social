import requests


def create_image_post(page_id, page_access_token, image_url):

    url = f"https://graph.facebook.com/v17.0/{page_id}/photos"

    headers = {
            "Authorization": f"Bearer {page_access_token}"
        }

    data = {
        "message": "This is an awesome image...",
        "url": image_url,
    }

    response = requests.post(url, headers=headers, data=data)

    if not response.json().get('error'):
        print("Image posted successfully...")

    else:
        print("Image could not be posted...")
        error = response.json().get('error')
        return {'error': error}

    return response.json()


if __name__ == '__main__':

    _page_id = "103658366092003"
    _image_url = "https://cdn.pixabay.com/photo/2015/03/10/17/23/youtube-667451_960_720.png"
    _page_access_token = "EAAathGdn1gcBOZBoQCq8Cogy4YUBSjT7iKqZAyQW7nTxJUmVX2zgskd16ZCwsVyN3HQZCuKuYvog7SBRPJHMflgZCrkIJA4VXL2d7At7VTRuRVIFGqBzS7H3Cg5JsS1fveYZAhtDK41O0lQfphiGJqyy8hAO7kR1rI2sea3hAenLx3ZBzJZC9WD95DDR2JyiBXfxtOd7kqQZD"

    create_image_post_response = create_image_post(_page_id, _page_access_token, _image_url)

    print(create_image_post_response)
