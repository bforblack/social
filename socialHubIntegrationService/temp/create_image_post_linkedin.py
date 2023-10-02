import requests
import base64
from io import BytesIO


def generate_image_url(url, access_token, author):

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {access_token}"
    }

    data = {
        "initializeUploadRequest": {
            "owner": author
        }
    }

    response = requests.post(url, headers=headers, json=data)

    if response.status_code != 200:
        print("Error ocurred while generating upload url for Linkedin image post...")
        error = response.json().get('message')
        return {'error': error}

    return response.json()


def upload_data(image_upload_data, access_token, base64_image_data):

    url = image_upload_data.get('value').get('uploadUrl')

    headers = {
        "Authorization": f"Bearer {access_token}"
    }

    decoded_image_data = base64.b64decode(base64_image_data)

    image_file = BytesIO(decoded_image_data)

    files = {
        "file": ("image.jpg", image_file)
    }

    response = requests.post(url, headers=headers, files=files)

    if response.status_code != 201:
        error = "Image upload failed..."
        print(error)
        return {'error': error}
    else:
        print("Image uploaded successfully...")
        return {'upload': 'success'}


def post_image_data(url, access_token, author, post, image_title, image_id):

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
                "altText": image_title,
                "id": image_id
            }
        },

        "lifecycleState": "PUBLISHED",
        "isReshareDisabledByAuthor": False
    }

    response = requests.post(url, headers=headers, json=data)

    if response.status_code != 201:
        error = response.json().get('message')
        return {'error': error}
    else:
        post_id = response.headers.get('x-linkedin-id')
        post_data = {'post_status': 'success', 'post_id': post_id}
        return post_data


if __name__ == '__main__':

    _url = "https://api.linkedin.com/v2/posts"
    _upload_url = "https://api.linkedin.com/v2/images?action=initializeUpload"
    _access_token = "AQX_qX5ti8iEIo5tuuNa2jarpRtxcnylBDR9ylI6oT2sdxLju-lTK8w0RUSFMuo31qIRF_DJ56J9YcA-DPDL1SAX-FYiDiMzgwwoDwJDimoxwHbQKpPrvd0ZdlF7v05Vv0JEG_wg3RaNR2Xt5QlU86GYx9a_-ZolTgA5Env_wkN4wcoUuhPOpxsBNSec5y8cHD9zw7i1RHIm3Tc8bcQN_IxOrX4mLLsgSLrDYrI_dJoWfVv6oBx6JGYCjj_4_AyAyC5o89PHjK7lye5stK9DCgAZ7i2lVeW6PnCmvuR0RAv0Is9-2Q7ZJYBdk09QRPYDJpoczGckdGCfWgqJyUGHvg2Uqmlz4Q"
    _author = "urn:li:organization:96072893"
    _post = "This is a beautiful picture!"
    _image_title = "Beautiful picture!"

    upload_file_path = "../multimedia/image.jpg"
    with open(upload_file_path, "rb") as file:
        _base64_image_data = base64.b64encode(file.read()).decode()

    generate_url_response_data = generate_image_url(_upload_url, _access_token, _author)

    if not generate_url_response_data.get('error'):
        uploaded = upload_data(image_upload_data=generate_url_response_data, access_token=_access_token, base64_image_data=_base64_image_data)

        if not uploaded.get('error'):
            _image_id = generate_url_response_data.get('value').get('image')

            posted = post_image_data(_url, _access_token, _author, _post, _image_title, _image_id)

            if not posted.get('error'):
                print('Image post successfully posted on Linkedin...')

            else:
                print('Image post could not be posted on Linkedin...')

        else:
            print(uploaded)

    else:
        print(generate_url_response_data)

# {'value': {'uploadUrlExpiresAt': 1690628556773, 'uploadUrl': 'https://www.linkedin.com/dms-uploads/sp/D4D10AQGGOMmXlC_16A/uploaded-image/0?ca=vector_ads&cn=uploads&sync=0&v=beta&ut=0vztBaLL5mXqQ1', 'image': 'urn:li:image:D4D10AQGGOMmXlC_16A'}}
