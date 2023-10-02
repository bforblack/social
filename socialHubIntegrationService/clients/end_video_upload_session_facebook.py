import requests


def finish_video_upload_session(page_id, access_token, upload_session_id):

    url = f"https://graph.facebook.com/v17.0/{page_id}/videos"

    params = {
        "upload_phase": "finish",
        "access_token": access_token,
        "upload_session_id": upload_session_id
    }

    data = {
        "description": "This is the description...",
        "title": "This is the title..."
    }

    response = requests.post(url, params=params, data=data)
    return response.json()


if __name__ == "__main__":
    # Replace these variables with actual values
    _page_id = "103658366092003"
    _access_token = "EAAathGdn1gcBOZBoQCq8Cogy4YUBSjT7iKqZAyQW7nTxJUmVX2zgskd16ZCwsVyN3HQZCuKuYvog7SBRPJHMflgZCrkIJA4VXL2d7At7VTRuRVIFGqBzS7H3Cg5JsS1fveYZAhtDK41O0lQfphiGJqyy8hAO7kR1rI2sea3hAenLx3ZBzJZC9WD95DDR2JyiBXfxtOd7kqQZD"
    _upload_session_id = "300382109108792"

    response_data = finish_video_upload_session(_page_id, _access_token, _upload_session_id)
    print(response_data)

# {'success': True}
