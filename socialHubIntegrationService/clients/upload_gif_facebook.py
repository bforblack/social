import requests


def upload_video_chunk(page_id, upload_session_id, access_token, start_offset, video_file_path):
    url = f"https://graph-video.facebook.com/v17.0/{page_id}/videos"

    params = {
        "upload_phase": "transfer",
        "upload_session_id": upload_session_id,
        "access_token": access_token,
        "start_offset": start_offset,
    }

    data = {
        "caption": "This video is awesome...",
        "description": "This is the description...",
        "title": "This is the title..."
    }

    files = {
        "video_file_chunk": open(video_file_path, "rb")
    }

    response = requests.post(url, params=params, files=files, data=data)
    return response.json()


if __name__ == "__main__":
    # Replace these variables with actual values

    _page_id = "103658366092003"
    _upload_session_id = "994220078668257"
    _access_token = "EAAathGdn1gcBOZBoQCq8Cogy4YUBSjT7iKqZAyQW7nTxJUmVX2zgskd16ZCwsVyN3HQZCuKuYvog7SBRPJHMflgZCrkIJA4VXL2d7At7VTRuRVIFGqBzS7H3Cg5JsS1fveYZAhtDK41O0lQfphiGJqyy8hAO7kR1rI2sea3hAenLx3ZBzJZC9WD95DDR2JyiBXfxtOd7kqQZD"
    _start_offset = 0
    _video_file_path = "/home/sumit/Desktop/postManagementService/DataNext/src/python/social/socialHubIntegrationService/multimedia/gif.gif"  # Replace with the actual path to your video file

    response_data = upload_video_chunk(_page_id, _upload_session_id, _access_token, _start_offset, _video_file_path)

    print(response_data)

# {'start_offset': '43130784', 'end_offset': '43130784'}
