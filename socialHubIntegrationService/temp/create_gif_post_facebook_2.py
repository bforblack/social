import requests
import os
import base64
from io import BytesIO


def create_gif_upload_session(url, access_token, file_size):

    params = {
        "upload_phase": "start",
        "access_token": access_token,
        "file_size": file_size
    }

    response = requests.post(url, params=params)

    if not response.json().get('error'):
        print("gif upload session successfully created...")
        return response.json()

    else:
        print("gif upload session could not be created...")
        error = {"error": response.json().get('error')}
        return error


def upload_gif(url, upload_session_id, access_token, start_offset, gif_file):

    params = {
        "upload_phase": "transfer",
        "upload_session_id": upload_session_id,
        "access_token": access_token,
        "start_offset": start_offset,
    }

    files = {
        "video_file_chunk": gif_file
    }

    response = requests.post(url, params=params, files=files)

    if not response.json().get('error'):
        print("gif upload completed successfully..")
        return response.json()

    else:
        print("gif upload failed..")
        error = {"error": response.json().get('error')}
        return error


def finish_gif_upload_session(url, access_token, upload_session_id, post, gif_title):

    params = {
        "upload_phase": "finish",
        "access_token": access_token,
        "upload_session_id": upload_session_id
    }

    data = {
        "description": post,
        "title": gif_title
    }

    response = requests.post(url, params=params, data=data)

    if not response.json().get('error'):
        print("gif upload session ended successfully...")
        return response.json()

    else:
        print("gif upload session could not be ended...")
        error = {"error": response.json().get('error')}
        return error


if __name__ == "__main__":

    _gif_file_path = "../multimedia/gif.gif"
    with open(_gif_file_path, "rb") as file:
        _base64_image_data = base64.b64encode(file.read()).decode()
    decoded_image_data = base64.b64decode(_base64_image_data)
    _gif_file = BytesIO(decoded_image_data)
    _file_size = len(_gif_file.getvalue())

    _page_id = "103658366092003"
    _upload_session_url = f"https://graph.facebook.com/v17.0/{_page_id}/videos"
    _upload_gif_url = f"https://graph-video.facebook.com/v17.0/{_page_id}/videos"
    _end_session_url = f"https://graph.facebook.com/v17.0/{_page_id}/videos"

    _access_token = "EAAathGdn1gcBOZBoQCq8Cogy4YUBSjT7iKqZAyQW7nTxJUmVX2zgskd16ZCwsVyN3HQZCuKuYvog7SBRPJHMflgZCrkIJA4VXL2d7At7VTRuRVIFGqBzS7H3Cg5JsS1fveYZAhtDK41O0lQfphiGJqyy8hAO7kR1rI2sea3hAenLx3ZBzJZC9WD95DDR2JyiBXfxtOd7kqQZD"

    _post = "This is the gif description..."
    _gif_title = "This is the gif title..."

    create_session_response_data = create_gif_upload_session(_upload_session_url, _access_token, _file_size)

    if not create_session_response_data.get('error'):

        _video_id = create_session_response_data.get('video_id')
        _start_offset = create_session_response_data.get('start_offset')
        _end_offset = create_session_response_data.get('end_offset')
        _upload_session_id = create_session_response_data.get('upload_session_id')

        upload_gif_response_data = upload_gif(_upload_gif_url, _upload_session_id, _access_token, _start_offset,
                                              _gif_file)

        if not upload_gif_response_data.get('error'):
            end_session_response_data = finish_gif_upload_session(_end_session_url, _access_token, _upload_session_id, _post, _gif_title)

            if not end_session_response_data.get('error'):
                print("gif post created successfully...")
                print(end_session_response_data)

            else:
                print(end_session_response_data)

        else:
            print(upload_gif_response_data)

    else:
        print(create_session_response_data)

# {'video_id': '300382102442126', 'start_offset': '0', 'end_offset': '1048576', 'upload_session_id': '300382109108792'}
