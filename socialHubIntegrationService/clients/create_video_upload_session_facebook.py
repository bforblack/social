import requests
import os


def start_video_upload(page_id, access_token, file_size):

    url = f"https://graph.facebook.com/v17.0/{page_id}/videos"

    params = {
        "upload_phase": "start",
        "access_token": access_token,
        "file_size": file_size
    }

    data = {
        "caption": "This video is awesome...",
        "description": "This is the description...",
        "title": "This is the title... Though not the one to look into the darkness, it seems that I am the GOAT..."
    }

    response = requests.post(url, params=params, data=data)

    return response.json()


if __name__ == "__main__":

    _file_path = "/home/sumit/Desktop/postManagementService/DataNext/src/python/social/socialHubIntegrationService/multimedia/video.mp4"
    _file_size = os.stat(_file_path).st_size

    _page_id = "103658366092003"
    _access_token = "EAAathGdn1gcBOZBoQCq8Cogy4YUBSjT7iKqZAyQW7nTxJUmVX2zgskd16ZCwsVyN3HQZCuKuYvog7SBRPJHMflgZCrkIJA4VXL2d7At7VTRuRVIFGqBzS7H3Cg5JsS1fveYZAhtDK41O0lQfphiGJqyy8hAO7kR1rI2sea3hAenLx3ZBzJZC9WD95DDR2JyiBXfxtOd7kqQZD"

    response_data = start_video_upload(_page_id, _access_token, _file_size)

    print(response_data)

# {'video_id': '300382102442126', 'start_offset': '0', 'end_offset': '1048576', 'upload_session_id': '300382109108792'}
