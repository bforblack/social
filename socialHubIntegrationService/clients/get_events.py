import requests


def get_user_data(url, access_token):
    try:
        headers = {
            'Authorization': f'Bearer {access_token}',
            'X-Restli-Protocol-Version': '2.0.0',
            'LinkedIn-Version': '202304'
        }

        response = requests.request("GET", url, headers=headers)

        if response.status_code == 200:
            print("Received successful response from get_user_data() call to LinkedIn API...")
            data = response.json()
            return data
        else:
            print(
                f"Received negative response from LinkedIn while making get_user_data call to LinkedIn API: {response.text}")
            return {"error_message": response.text}

    except Exception as e:
        print(f"An Exception occurred while making get_user_data() call to LinkedIn API: {e}")
        return {"error_message": e}


if __name__ == "__main__":
    # _url = "https://api.linkedin.com/v2/events?organizer=urn:li:organization:96072893&q=organizerLeadGenFormEnabledEvents&start=0&count=2"
    _url = "https://api.linkedin.com/rest/events/7087030501919629312"
    _access_token = "AQX_qX5ti8iEIo5tuuNa2jarpRtxcnylBDR9ylI6oT2sdxLju-lTK8w0RUSFMuo31qIRF_DJ56J9YcA-DPDL1SAX-FYiDiMzgwwoDwJDimoxwHbQKpPrvd0ZdlF7v05Vv0JEG_wg3RaNR2Xt5QlU86GYx9a_-ZolTgA5Env_wkN4wcoUuhPOpxsBNSec5y8cHD9zw7i1RHIm3Tc8bcQN_IxOrX4mLLsgSLrDYrI_dJoWfVv6oBx6JGYCjj_4_AyAyC5o89PHjK7lye5stK9DCgAZ7i2lVeW6PnCmvuR0RAv0Is9-2Q7ZJYBdk09QRPYDJpoczGckdGCfWgqJyUGHvg2Uqmlz4Q"
    _data = get_user_data(_url, _access_token)
    print(_data)

