import requests


access_token = "AQX_qX5ti8iEIo5tuuNa2jarpRtxcnylBDR9ylI6oT2sdxLju-lTK8w0RUSFMuo31qIRF_DJ56J9YcA-DPDL1SAX-FYiDiMzgwwoDwJDimoxwHbQKpPrvd0ZdlF7v05Vv0JEG_wg3RaNR2Xt5QlU86GYx9a_-ZolTgA5Env_wkN4wcoUuhPOpxsBNSec5y8cHD9zw7i1RHIm3Tc8bcQN_IxOrX4mLLsgSLrDYrI_dJoWfVv6oBx6JGYCjj_4_AyAyC5o89PHjK7lye5stK9DCgAZ7i2lVeW6PnCmvuR0RAv0Is9-2Q7ZJYBdk09QRPYDJpoczGckdGCfWgqJyUGHvg2Uqmlz4Q"

activity_id = 'urn%3Ali%3Aactivity%3A7095684521727016961'

urls = [f"https://api.linkedin.com/v2/activities?ids={activity_id}"]

headers = {
    "Authorization": f"Bearer {access_token}",
}

if __name__ == '__main__':

    for url in urls:

        response = requests.get(url, headers=headers)

        if response.status_code == 200:

            print("Source Activity Info:")
            print(response.text)

        else:
            print("Failed to fetch Information:", response.status_code, response.text)
