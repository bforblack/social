from pojos.Oculus_pojo import Oculus


if __name__ == "__main__":
    _request = {
        "_id": "123",
        "username": "sumitbutola",
        "registrationId": "abc-cde-def-efg-fgh-ghi",

        "faceBook": {
            "appId": "105597722562611",
            "accessToken": "EAAathGdn1gcBAP1UOXetoaqExF8WaTHT2KWASDf4ZCf9mlqjB1CJfZBwhCIALaQmjKsZCeFKmmZAAhoZBv0sezOBnKDkOMVH9WmipPN5PbnvQ6ZBjB32aTShZAPbXebZBZCJZC1K6rYUEWZCf61HzxYTyWIO8uraZAoOyZBi7Mvsx4zh3VZAZBbJHYLkBRDDeBUKZBTn4g2LdJr57qS9sc1GGbu9MoUG"
        },

        "instagram": {
            "appId": "a67df903-4eae-4bb3-9ed8-4afe38028fe2",
            "accessToken": "Hello"
        },

        "twitter": {
            "bearerToken": "AAAAAAAAAAAAAAAAAAAAAO5anwEAAAAAAg7Yq3LHcT8GHU9CdUM9Xdnx%2Bpk%3DUw9bVcY62kCdBrMvPLpumrceyWCpDcv8ThyNd5L8ibHRVukxXq",
            "apiKey": "rlK5eBq5FiaCjIl1HNQYj8tIl",
            "apiKeySecret": "9VCDYva7ymUtFhukFoZJksr2BKoIXm4zFpLbwIym6ikWKEssRH",
            "accessToken": "1660903613076758528-rGhNMF88anjfG0GpVnpfNYZY9RQl1J",
            "accessTokenSecret": "oy761O8aJqCW1mdfqGBAuak2gULNA5t4NXJhTLLkoNDfK"
        },

        "linkedIn": {
            "appId": "9842754e-7866-4d94-aae5-39adecf7dc25",
            "accessToken": "AQX_qX5ti8iEIo5tuuNa2jarpRtxcnylBDR9ylI6oT2sdxLju-lTK8w0RUSFMuo31qIRF_DJ56J9YcA-DPDL1SAX-FYiDiMzgwwoDwJDimoxwHbQKpPrvd0ZdlF7v05Vv0JEG_wg3RaNR2Xt5QlU86GYx9a_-ZolTgA5Env_wkN4wcoUuhPOpxsBNSec5y8cHD9zw7i1RHIm3Tc8bcQN_IxOrX4mLLsgSLrDYrI_dJoWfVv6oBx6JGYCjj_4_AyAyC5o89PHjK7lye5stK9DCgAZ7i2lVeW6PnCmvuR0RAv0Is9-2Q7ZJYBdk09QRPYDJpoczGckdGCfWgqJyUGHvg2Uqmlz4Q"
        }
    }
    response = Oculus(**_request).register_user()

    # print(response)
