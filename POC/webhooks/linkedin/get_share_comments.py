import requests
import json

access_token = "AQX_qX5ti8iEIo5tuuNa2jarpRtxcnylBDR9ylI6oT2sdxLju-lTK8w0RUSFMuo31qIRF_DJ56J9YcA-DPDL1SAX-FYiDiMzgwwoDwJDimoxwHbQKpPrvd0ZdlF7v05Vv0JEG_wg3RaNR2Xt5QlU86GYx9a_-ZolTgA5Env_wkN4wcoUuhPOpxsBNSec5y8cHD9zw7i1RHIm3Tc8bcQN_IxOrX4mLLsgSLrDYrI_dJoWfVv6oBx6JGYCjj_4_AyAyC5o89PHjK7lye5stK9DCgAZ7i2lVeW6PnCmvuR0RAv0Is9-2Q7ZJYBdk09QRPYDJpoczGckdGCfWgqJyUGHvg2Uqmlz4Q"
entity = "urn:li:share:7095684521320169472"

url = f"https://api.linkedin.com/rest/socialActions/{entity}/comments"

headers = {
    "Authorization": f"Bearer {access_token}",
    "Content-Type": "application/json",
    "LinkedIn-Version": "202306"
}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    data = response.json()
    beautified_json = json.dumps(data, indent=4)
    print(beautified_json)
else:
    print(f"Request failed with status code: {response.status_code}")
    print(response.text)
