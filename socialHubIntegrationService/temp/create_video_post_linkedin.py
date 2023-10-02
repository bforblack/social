import requests
import os


def initialize_linkedin_video_upload(access_token, video_initialize_upload_url, video_url):
    try:
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {access_token}"
        }

        data = {
            "initializeUploadRequest": {
                "owner": "urn:li:organization:96072893",
                "fileSizeBytes": os.stat(video_url).st_size,
                "uploadCaptions": False,
                "uploadThumbnail": False
            }
        }

        response = requests.post(video_initialize_upload_url, headers=headers, json=data)
        response_json = response.json()

        if response.status_code == 200:
            return response_json
        else:
            error_message = response_json.get('message', 'Unknown error')
            return {"error": error_message}

    except Exception as e:
        return {"error": str(e)}


def split_file(file_path, chunk_size):
    with open(file_path, 'rb') as f:
        while True:
            chunk = f.read(chunk_size)
            if not chunk:
                break
            yield chunk


def upload_video_to_linkedin(access_token, video_url, upload_urls):
    try:
        chunk_size = 4194303
        uploaded_part_ids = []

        headers = {
            "Authorization": f"Bearer {access_token}",
            "Content-Type": "application/octet-stream"
        }

        chunk_number = 1
        chunks = split_file(video_url, chunk_size)

        for chunk in chunks:
            current_upload_url = upload_urls[chunk_number - 1]
            response = requests.post(current_upload_url, data=chunk, headers=headers)

            print(f"Chunk {chunk_number}, Status Code: {response.status_code}, etag: {response.headers.get('etag')}")

            uploaded_part_ids.append(response.headers.get('etag'))
            chunk_number += 1

            if chunk_number > len(upload_urls):
                break

        return {'uploaded_part_ids': uploaded_part_ids}

    except Exception as e:
        return {"error": str(e)}


def finalize_linkedin_video(access_token, video_finalize_upload_url, final_video_urn, uploaded_part_ids):

    json_data = {
        "finalizeUploadRequest": {
            "video": final_video_urn,
            "uploadToken": "",
            "uploadedPartIds": uploaded_part_ids
        }
    }

    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json",
        'LinkedIn-Version': '202306',
        'X-Restli-Protocol-Version': '2.0.0'
    }

    response = requests.post(video_finalize_upload_url, json=json_data, headers=headers)

    print(f"Response Status Code: {response.status_code}")

    if response.status_code == 200:
        return {"post": "success"}

    else:
        return {
            "error": f"Video upload finalize request failed with status code: {response.status_code} Error: {response.text}"
        }


def create_linkedin_post(access_token, author, final_video_urn, post, url):

    try:
        headers = {
            "Authorization": f"Bearer {access_token}",
            "Content-Type": "application/json"
        }

        data = {
            "author": author,
            "commentary": post,
            "visibility": "PUBLIC",
            "distribution": {
                "feedDistribution": "MAIN_FEED",
                "targetEntities": [],
                "thirdPartyDistributionChannels": []
            },

            "content": {
                "media": {
                    "id": final_video_urn
                }
            },

            "lifecycleState": "PUBLISHED",
            "isReshareDisabledByAuthor": False
        }

        response = requests.post(url, headers=headers, json=data)

        if response.status_code != 201:
            error = {
                "error": f"Video post request failed with status code: {response.status_code} Error: {response.text}"
            }
            return error

        else:
            post_id = response.headers.get('x-linkedin-id')
            post_data = {'post_status': 'success', 'post_id': post_id}
            return post_data

    except Exception as e:
        error = {
            "error": str(e)
        }
        return error


if __name__ == '__main__':
    author = "urn:li:organization:96072893"
    url = "https://api.linkedin.com/v2/posts"
    post = "This is a video 001..."
    access_token = "AQX_qX5ti8iEIo5tuuNa2jarpRtxcnylBDR9ylI6oT2sdxLju-lTK8w0RUSFMuo31qIRF_DJ56J9YcA-DPDL1SAX-FYiDiMzgwwoDwJDimoxwHbQKpPrvd0ZdlF7v05Vv0JEG_wg3RaNR2Xt5QlU86GYx9a_-ZolTgA5Env_wkN4wcoUuhPOpxsBNSec5y8cHD9zw7i1RHIm3Tc8bcQN_IxOrX4mLLsgSLrDYrI_dJoWfVv6oBx6JGYCjj_4_AyAyC5o89PHjK7lye5stK9DCgAZ7i2lVeW6PnCmvuR0RAv0Is9-2Q7ZJYBdk09QRPYDJpoczGckdGCfWgqJyUGHvg2Uqmlz4Q"
    video_initialize_upload_url = "https://api.linkedin.com/v2/videos?action=initializeUpload"
    video_url = "../multimedia/video.mp4"
    video_finalize_upload_url = "https://api.linkedin.com/v2/videos?action=finalizeUpload"

    upload_information = initialize_linkedin_video_upload(access_token, video_initialize_upload_url, video_url)

    upload_urls = []

    if not upload_information.get('error'):

        final_video_urn = upload_information.get('value').get('video')

        for upload_url_info in upload_information.get('value').get('uploadInstructions'):
            upload_url = upload_url_info.get('uploadUrl')
            upload_urls.append(upload_url)

        uploaded = upload_video_to_linkedin(access_token, video_url, upload_urls)

        if not uploaded.get('error'):
            print("Uploaded: ")
            print(uploaded)

            uploaded_part_ids = uploaded.get('uploaded_part_ids')
            finalize_upload = finalize_linkedin_video(access_token, video_finalize_upload_url, final_video_urn, uploaded_part_ids)

            if not finalize_upload.get('error'):
                print("Finalize Upload: ")
                print(finalize_upload)

                posted = create_linkedin_post(access_token, author, final_video_urn, post, url)

                if not posted.get('error'):
                    print(posted)
                    print("Video post created...")
                else:
                    print(posted)
                    print("Video post failed...")

            else:
                print(finalize_upload)
                print("Video upload could not be finalized...")

        else:
            print("Video could not be uploaded...")

    else:
        print(upload_information)
        print("Video upload urls could not be generated...")


