import requests

if __name__ == '__main__':

    url = "https://api.linkedin.com/v2/posts"

    access_token = "AQUbm7y21qwnzeBnN1grSOlE5UEodWPh3gQ8wFDK94BhgLA3Gmi0LNX9UPByHthZvVlkagxT7DHp_ONSFc4uhqXApnHrO2ASo6J5_4jSzvFp4EZeWsflqdjQWHy0g3mZ7CcOtNERoWiXg6_jPVY8nXPA55gIIu9z8EERRcLYNRrOP3QZQjzRdrWd4VQeWyEeuFcCjrO4Vfg8NyxN-Dgy8jBpPiczbXyhHXBBGssdrpFmcK5Z24X-NzBq3a2GfYRaUeOLFOmnhoELFmwGt1d8ghEDRn4-HFitCMUR1i08u82Px-CJYP8a7oqOq1IuXBHTwzwx6aK1b5ypWBlUCvSd4R3CbTo5kQ"

    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json"
    }

    data = {
        "author": "urn:li:organization:96072893",
        "commentary": "This video is awesome as well...",
        "visibility": "PUBLIC",
        "distribution": {
            "feedDistribution": "MAIN_FEED",
            "targetEntities": [],
            "thirdPartyDistributionChannels": []
        },

        "content": {
            "media": {
                "id": "urn:li:video:D4D10AQGv5IUzIJeXuw"
            }
        },

        "lifecycleState": "PUBLISHED",
        "isReshareDisabledByAuthor": False
    }

    response = requests.post(url, headers=headers, json=data)
    print(response.status_code)

