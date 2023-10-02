import requests
import os


def start_gif_upload(page_id, access_token, file_size):

    url = f"https://graph.facebook.com/v17.0/{page_id}/videos"

    params = {
        "upload_phase": "start",
        "access_token": access_token,
        "file_size": file_size
    }

    data = {
        "caption": "This video is awesome...",
        "description": "This is the description...",
        "title": "This is the title..."
    }

    response = requests.post(url, params=params, data=data)

    return response.json()


if __name__ == "__main__":

    _file_path = "/home/sumit/Desktop/postManagementService/DataNext/src/python/social/socialHubIntegrationService/multimedia/gif.gif"
    _file_size = os.stat(_file_path).st_size

    _page_id = "103658366092003"
    _access_token = "EAAathGdn1gcBOZBoQCq8Cogy4YUBSjT7iKqZAyQW7nTxJUmVX2zgskd16ZCwsVyN3HQZCuKuYvog7SBRPJHMflgZCrkIJA4VXL2d7At7VTRuRVIFGqBzS7H3Cg5JsS1fveYZAhtDK41O0lQfphiGJqyy8hAO7kR1rI2sea3hAenLx3ZBzJZC9WD95DDR2JyiBXfxtOd7kqQZD"

    response_data = start_gif_upload(_page_id, _access_token, _file_size)

    print(response_data)

# {'video_id': '994220072001591', 'start_offset': '0', 'end_offset': '355854', 'upload_session_id': '994220078668257'}

