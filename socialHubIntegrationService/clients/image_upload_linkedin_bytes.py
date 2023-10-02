import requests
import base64
from io import BytesIO


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


if __name__ == '__main__':

    _image_upload_data = {'value': {'uploadUrlExpiresAt': 1690875921291,
                                    'uploadUrl': 'https://www.linkedin.com/dms-uploads/sp/D4D10AQGTgx7R2spG8A/uploaded-image/0?ca=vector_ads&cn=uploads&sync=0&v=beta&ut=2Ut72YcidN_qQ1',
                                    'image': 'urn:li:image:D4D10AQGTgx7R2spG8A'}}

    upload_file_path = "../multimedia/image.jpg"
    with open(upload_file_path, "rb") as file:
        _base64_image_data = base64.b64encode(file.read()).decode()

    _access_token = "AQX_qX5ti8iEIo5tuuNa2jarpRtxcnylBDR9ylI6oT2sdxLju-lTK8w0RUSFMuo31qIRF_DJ56J9YcA-DPDL1SAX-FYiDiMzgwwoDwJDimoxwHbQKpPrvd0ZdlF7v05Vv0JEG_wg3RaNR2Xt5QlU86GYx9a_-ZolTgA5Env_wkN4wcoUuhPOpxsBNSec5y8cHD9zw7i1RHIm3Tc8bcQN_IxOrX4mLLsgSLrDYrI_dJoWfVv6oBx6JGYCjj_4_AyAyC5o89PHjK7lye5stK9DCgAZ7i2lVeW6PnCmvuR0RAv0Is9-2Q7ZJYBdk09QRPYDJpoczGckdGCfWgqJyUGHvg2Uqmlz4Q"

    uploaded = upload_data(_image_upload_data, _access_token, _base64_image_data)


