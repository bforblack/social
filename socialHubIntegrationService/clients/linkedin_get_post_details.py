import json

from socialhub.oculusconnectorsapi.linkedin_api import LinkedInAPI


def get_user_data(post_urn, access_token):
    url = f"https://api.linkedin.com/v2/posts/{post_urn}"
    response = LinkedInAPI(accessToken=access_token).get_user_data(url=url)

    return response


if __name__ == "__main__":
    _post_urn = "urn:li:share:7087723491524845569"
    _access_token = "AQX_qX5ti8iEIo5tuuNa2jarpRtxcnylBDR9ylI6oT2sdxLju-lTK8w0RUSFMuo31qIRF_DJ56J9YcA-DPDL1SAX-FYiDiMzgwwoDwJDimoxwHbQKpPrvd0ZdlF7v05Vv0JEG_wg3RaNR2Xt5QlU86GYx9a_-ZolTgA5Env_wkN4wcoUuhPOpxsBNSec5y8cHD9zw7i1RHIm3Tc8bcQN_IxOrX4mLLsgSLrDYrI_dJoWfVv6oBx6JGYCjj_4_AyAyC5o89PHjK7lye5stK9DCgAZ7i2lVeW6PnCmvuR0RAv0Is9-2Q7ZJYBdk09QRPYDJpoczGckdGCfWgqJyUGHvg2Uqmlz4Q"
    _response = get_user_data(_post_urn, _access_token)
    print(_response)
