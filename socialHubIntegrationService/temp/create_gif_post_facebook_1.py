import requests
import os


def create_gif_upload_session(page_id, access_token, file_size):

    url = f"https://graph.facebook.com/v17.0/{page_id}/videos"

    params = {
        "upload_phase": "start",
        "access_token": access_token,
        "file_size": file_size
    }

    response = requests.post(url, params=params)

    if not response.json().get('error'):
        print("gif upload session successfully created...")

    else:
        print("gif upload session could not be created...")

    return response.json()


def upload_gif(page_id, upload_session_id, access_token, start_offset, gif_file_path):

    url = f"https://graph-video.facebook.com/v17.0/{page_id}/videos"

    params = {
        "upload_phase": "transfer",
        "upload_session_id": upload_session_id,
        "access_token": access_token,
        "start_offset": start_offset,
    }

    data = {
        "description": "This is the description..",
        "title": "This is the title.."
    }

    files = {
        "video_file_chunk": open(gif_file_path, "rb")
    }

    response = requests.post(url, params=params, files=files, data=data)

    if not response.json().get('error'):
        print("gif upload completed successfully...")

    else:
        print("gif upload failed...")

    return response.json()


def finish_gif_upload_session(page_id, access_token, upload_session_id):
    
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

    if not response.json().get('error'):
        print("gif upload session ended successfully...")

    else:
        print("gif upload session could not be ended...")

    return response.json()


if __name__ == "__main__":

    _gif_file_path = "/home/sumit/Desktop/postManagementService/DataNext/src/python/social/socialHubIntegrationService/multimedia/gif.gif"
    _file_size = os.stat(_gif_file_path).st_size

    _page_id = "103658366092003"

    _access_token = "EAAathGdn1gcBOZBoQCq8Cogy4YUBSjT7iKqZAyQW7nTxJUmVX2zgskd16ZCwsVyN3HQZCuKuYvog7SBRPJHMflgZCrkIJA4VXL2d7At7VTRuRVIFGqBzS7H3Cg5JsS1fveYZAhtDK41O0lQfphiGJqyy8hAO7kR1rI2sea3hAenLx3ZBzJZC9WD95DDR2JyiBXfxtOd7kqQZD"

    create_session_response_data = create_gif_upload_session(_page_id, _access_token, _file_size)

    if not create_session_response_data.get('error'):

        _video_id = create_session_response_data.get('video_id')
        _start_offset = create_session_response_data.get('start_offset')
        _end_offset = create_session_response_data.get('end_offset')
        _upload_session_id = create_session_response_data.get('upload_session_id')

        upload_gif_response_data = upload_gif(_page_id, _upload_session_id, _access_token, _start_offset, _gif_file_path)

        if not upload_gif_response_data.get('error'):
            end_session_response_data = finish_gif_upload_session(_page_id, _access_token, _upload_session_id)

            if not end_session_response_data.get('error'):
                print("Video post created successfully...")

            else:
                print(end_session_response_data)

        else:
            print(upload_gif_response_data)

    else:
        print(create_session_response_data)


# {'video_id': '300382102442126', 'start_offset': '0', 'end_offset': '1048576', 'upload_session_id': '300382109108792'}
