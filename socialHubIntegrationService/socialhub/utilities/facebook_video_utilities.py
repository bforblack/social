import requests
import os

from logs.studio_logger import Logger
logger = Logger("socialHubIntegrationService")


def create_video_upload_session(create_video_upload_session_url, access_token, file_size):

    logger.info("Creating facebook video upload session...")

    try:

        params = {
            "upload_phase": "start",
            "access_token": access_token,
            "file_size": file_size
        }

        response = requests.post(create_video_upload_session_url, params=params)

        if not response.json().get('error'):
            logger.info("Video upload session successfully created...")
            return response.json()

        else:
            error_message = f"Video upload session could not be created: {response.text}"
            logger.info(error_message)
            error = {"error": error_message}
            return error

    except Exception as e:
        error_message = f"Video upload session could not be created: {str(e)}"
        logger.info(error_message)
        error = {"error": error_message}
        return error


def upload_video_chunk(upload_video_chunk_url, upload_session_id, access_token, start_offset, video_url):

    logger.info("Uploading video chunks to facebook server...")

    try:

        params = {
            "upload_phase": "transfer",
            "upload_session_id": upload_session_id,
            "access_token": access_token,
            "start_offset": start_offset
        }

        files = {
            "video_file_chunk": open(video_url, "rb")
        }

        response = requests.post(upload_video_chunk_url, params=params, files=files)

        if not response.json().get('error'):
            logger.info("Video upload to facebook server completed successfully...")
            return response.json()

        else:
            error_message = f"gif upload to facebook server failed: {response.json().get('error')}"
            logger.info(error_message)
            error = {"error": error_message}
            return error

    except Exception as e:
        error_message = f"gif upload to facebook server failed: {str(e)}"
        logger.info(error_message)
        error = {"error": error_message}
        return error


def finish_video_upload_session(finish_video_upload_session_url, access_token, upload_session_id, post, video_title):

    logger.info("Finishing facebook gif upload session and creating video post...")

    try:
        params = {
            "upload_phase": "finish",
            "access_token": access_token,
            "upload_session_id": upload_session_id
        }

        data = {
            "description": post,
            "title": video_title
        }

        response = requests.post(finish_video_upload_session_url, params=params, data=data)

        if not response.json().get('error'):
            logger.info("Facebook video upload session ended and gif post created successfully...")
            return response.json()
        else:
            error_message = f"Facebook gif upload session could not be ended and gif post could not be created: {response.json().get('error')}"
            logger.info(error_message)
            error = {"error": error_message}
            return error

    except Exception as e:
        error_message = f"Facebook gif upload session could not be ended and gif post could not be created: {str(e)}"
        logger.info(error_message)
        error = {"error": error_message}
        return error


if __name__ == "__main__":

    video_url = "/home/sumit/Desktop/postManagementService/DataNext/src/python/social/socialHubIntegrationService/multimedia/video.mp4"
    file_size = os.stat(video_url).st_size

    page_id = "103658366092003"

    create_video_upload_session_url = f"https://graph.facebook.com/v17.0/{page_id}/videos"
    upload_video_chunk_url = f"https://graph-video.facebook.com/v17.0/{page_id}/videos"
    finish_video_upload_session_url = f"https://graph.facebook.com/v17.0/{page_id}/videos"

    access_token = "EAAathGdn1gcBOZBoQCq8Cogy4YUBSjT7iKqZAyQW7nTxJUmVX2zgskd16ZCwsVyN3HQZCuKuYvog7SBRPJHMflgZCrkIJA4VXL2d7At7VTRuRVIFGqBzS7H3Cg5JsS1fveYZAhtDK41O0lQfphiGJqyy8hAO7kR1rI2sea3hAenLx3ZBzJZC9WD95DDR2JyiBXfxtOd7kqQZD"

    post = "This is the description..."
    video_title = "This is the title..."

    create_session_response_data = create_video_upload_session(create_video_upload_session_url, access_token, file_size)

    if not create_session_response_data.get('error'):

        _video_id = create_session_response_data.get('video_id')
        start_offset = create_session_response_data.get('start_offset')
        _end_offset = create_session_response_data.get('end_offset')
        upload_session_id = create_session_response_data.get('upload_session_id')

        upload_video_response_data = upload_video_chunk(upload_video_chunk_url, upload_session_id, access_token, start_offset, video_url)

        if not upload_video_response_data.get('error'):
            end_session_response_data = finish_video_upload_session(finish_video_upload_session_url, access_token, upload_session_id, post, video_title)

            if not end_session_response_data.get('error'):
                print("Video post created successfully...")

            else:
                print(end_session_response_data)

        else:
            print(upload_video_response_data)

    else:
        print(create_session_response_data)


# {'video_id': '300382102442126', 'start_offset': '0', 'end_offset': '1048576', 'upload_session_id': '300382109108792'}
