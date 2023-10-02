import json
import requests


def post_text(url, author, post, access_token):
    try:
        payload = json.dumps({
            "author": author,
            "commentary": post,
            "visibility": "PUBLIC",
            "distribution": {
                "feedDistribution": "MAIN_FEED",
                "targetEntities": [],
                "thirdPartyDistributionChannels": []
            },
            "lifecycleState": "PUBLISHED",
            "isReshareDisabledByAuthor": False
        })

        headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {access_token}',
        }

        response = requests.post(url, headers=headers, data=payload)

        if response.status_code == 201:
            print("Received successful response from post_data call to Linkedin API...")
            post_id = response.headers.get('x-linkedin-id')
            post_data = {'post_status': 'success', 'post_id': post_id}
            return post_data
        else:
            print(
                f"Received negative response from LinkedIn while making post_data call to LinkedIn API: {response.text}")
            return {"error": response.text}

    except Exception as e:
        print(f"An Exception occurred while making post_data() call to LinkedIn API: {str(e)}")
        return {"error": str(e)}


if __name__ == "__main__":
    _url = "https://api.linkedin.com/v2/posts"
    _author = "urn:li:organization:96072893"
    _post = "This is post from user..."
    _access_token = "AQUbm7y21qwnzeBnN1grSOlE5UEodWPh3gQ8wFDK94BhgLA3Gmi0LNX9UPByHthZvVlkagxT7DHp_ONSFc4uhqXApnHrO2ASo6J5_4jSzvFp4EZeWsflqdjQWHy0g3mZ7CcOtNERoWiXg6_jPVY8nXPA55gIIu9z8EERRcLYNRrOP3QZQjzRdrWd4VQeWyEeuFcCjrO4Vfg8NyxN-Dgy8jBpPiczbXyhHXBBGssdrpFmcK5Z24X-NzBq3a2GfYRaUeOLFOmnhoELFmwGt1d8ghEDRn4-HFitCMUR1i08u82Px-CJYP8a7oqOq1IuXBHTwzwx6aK1b5ypWBlUCvSd4R3CbTo5kQ"
    _response = post_text(_url, _author, _post, _access_token)
    print(_response)
