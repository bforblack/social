import requests

url = "https://api.linkedin.com/v2/posts"

access_token = "AQX_qX5ti8iEIo5tuuNa2jarpRtxcnylBDR9ylI6oT2sdxLju-lTK8w0RUSFMuo31qIRF_DJ56J9YcA-DPDL1SAX-FYiDiMzgwwoDwJDimoxwHbQKpPrvd0ZdlF7v05Vv0JEG_wg3RaNR2Xt5QlU86GYx9a_-ZolTgA5Env_wkN4wcoUuhPOpxsBNSec5y8cHD9zw7i1RHIm3Tc8bcQN_IxOrX4mLLsgSLrDYrI_dJoWfVv6oBx6JGYCjj_4_AyAyC5o89PHjK7lye5stK9DCgAZ7i2lVeW6PnCmvuR0RAv0Is9-2Q7ZJYBdk09QRPYDJpoczGckdGCfWgqJyUGHvg2Uqmlz4Q"

headers = {
    "Authorization": f"Bearer {access_token}",
    "Content-Type": "application/json"
}

data = {
    "author": "urn:li:organization:96072893",
    "commentary": "test strings!",
    "visibility": "PUBLIC",
    "distribution": {
        "feedDistribution": "MAIN_FEED",
        "targetEntities": [],
        "thirdPartyDistributionChannels": []
    },

    "content": {
        "media": {
            "altText": "testing for alt tags",
            "id": "urn:li:image:D5610AQGP2P331-0r-A"
        }
    },

    "lifecycleState": "PUBLISHED",
    "isReshareDisabledByAuthor": False
}

response = requests.post(url, headers=headers, json=data)
print("Hello")
print(response.json())
