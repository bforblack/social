import requests

url = "https://api.linkedin.com/v2/images?action=initializeUpload"

access_token = "AQX_qX5ti8iEIo5tuuNa2jarpRtxcnylBDR9ylI6oT2sdxLju-lTK8w0RUSFMuo31qIRF_DJ56J9YcA-DPDL1SAX-FYiDiMzgwwoDwJDimoxwHbQKpPrvd0ZdlF7v05Vv0JEG_wg3RaNR2Xt5QlU86GYx9a_-ZolTgA5Env_wkN4wcoUuhPOpxsBNSec5y8cHD9zw7i1RHIm3Tc8bcQN_IxOrX4mLLsgSLrDYrI_dJoWfVv6oBx6JGYCjj_4_AyAyC5o89PHjK7lye5stK9DCgAZ7i2lVeW6PnCmvuR0RAv0Is9-2Q7ZJYBdk09QRPYDJpoczGckdGCfWgqJyUGHvg2Uqmlz4Q"

headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {access_token}"
}

data = {
    "initializeUploadRequest": {
        "owner": "urn:li:organization:96072893"
    }
}

response = requests.post(url, headers=headers, json=data)
print(response.json())

image_data = {'value': {'uploadUrlExpiresAt': 1689325508508, 'uploadUrl': 'https://www.linkedin.com/dms-uploads/sp/D5610AQGP2P331-0r-A/uploaded-image/0?ca=vector_ads&cn=uploads&sync=0&v=beta&ut=2XWVARFTG1CaQ1', 'image': 'urn:li:image:D5610AQGP2P331-0r-A'}}

url = "https://www.linkedin.com/dms-uploads/C5622AQHdBDflPp0pEg/feedshare-uploadedImage/0?ca=vector_feedshare&cn=uploads&sync=1&v=beta&ut=1lrKqjt4fYuqw1"

upload_file_path = "/home/sumit/Desktop/postManagementService/DataNext/src/python/social/socialHubIntegrationService/multimedia/artbreeder-image.jpg"

access_token = f"Bearer {access_token}"

headers = {
    "Authorization": access_token
}

with open(upload_file_path, "rb") as file:
    files = {
        "file": file
    }

    response = requests.post(url, headers=headers, files=files)

# Handle the response
print("Response status code:", response.status_code)
print("Response content:", response.content.decode())
