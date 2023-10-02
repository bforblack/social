from pojos.Oculus_pojo import Oculus


if __name__ == "__main__":
    _request = {
        "pageId": "96072893",
        "accessToken": "{\"bearerToken\":\"AAAAAAAAAAAAAAAAAAAAAO5anwEAAAAAAg7Yq3LHcT8GHU9CdUM9Xdnx%2Bpk%3DUw9bVcY62kCdBrMvPLpumrceyWCpDcv8ThyNd5L8ibHRVukxXq\",\"apiKey\":\"rlK5eBq5FiaCjIl1HNQYj8tIl\",\"apiKeySecret\":\"9VCDYva7ymUtFhukFoZJksr2BKoIXm4zFpLbwIym6ikWKEssRH\",\"accessToken\":\"1660903613076758528-rGhNMF88anjfG0GpVnpfNYZY9RQl1J\",\"accessTokenSecret\":\"oy761O8aJqCW1mdfqGBAuak2gULNA5t4NXJhTLLkoNDfK\"}",
        "message": "This is my post 0017",
        "mediaSource": "twitter"
    }

    response = Oculus().post_data(_id="110928107339307_223939389918466", request=_request)

    # print(response)
