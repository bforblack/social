import streamlit as st


def run():
    mydict_i = {}
    with st.form("FaceBook"):
        # create three columns
        kpi1, kpi2, kpi3 = st.columns(3)

        kpi1.image(
            "https://upload.wikimedia.org/wikipedia/en/thumb/0/04/Facebook_f_logo_%282021%29.svg/2048px-Facebook_f_logo_%282021%29.svg.png",
            width=50)

        PageId_facebook_value = kpi1.text_input("**AppId**", value="105597722562611", key=1)

        accessToken_facebook = kpi1.text_input("**accessToken**",
                                               value="EAAathGdn1gcBAOYwyDGQyuFWqZCpfayZCm2lU00127pJ8YEPGc8tfQS8rQ9LmSAy97uUK0eGAwDDdqznH5gQDuD851zZAhrx4e7kegctTRHjMrfQC5HT6A6j9IHHe9M622svHUX7qs0DhCZBfDmZARX4TKE71wl8HW9gUsLGW5aOHO7jTHHcW",
                                               key=2)

        with kpi2.container():
            kpi2.image(
                "https://static-00.iconduck.com/assets.00/linkedin-icon-2048x2048-ya5g47j2.png",
                width=50)

            PageId_linkedin = kpi2.text_input("**AppId**", value="96072893", key=3)

            accessToken_linkedin = kpi2.text_input("**accessToken**",
                                                   value="AQX_qX5ti8iEIo5tuuNa2jarpRtxcnylBDR9ylI6oT2sdxLju-lTK8w0RUSFMuo31qIRF_DJ56J9YcA-DPDL1SAX-FYiDiMzgwwoDwJDimoxwHbQKpPrvd0ZdlF7v05Vv0JEG_wg3RaNR2Xt5QlU86GYx9a_-ZolTgA5Env_wkN4wcoUuhPOpxsBNSec5y8cHD9zw7i1RHIm3Tc8bcQN_IxOrX4mLLsgSLrDYrI_dJoWfVv6oBx6JGYCjj_4_AyAyC5o89PHjK7lye5stK9DCgAZ7i2lVeW6PnCmvuR0RAv0Is9-2Q7ZJYBdk09QRPYDJpoczGckdGCfWgqJyUGHvg2Uqmlz4Q",
                                                   key=4)

        with kpi3.container():
            kpi3.image(
                "https://png.pngtree.com/png-vector/20221018/ourmid/pngtree-twitter-social-media-round-icon-png-image_6315985.png",
                width=50)

            bearerToken_twitter = kpi3.text_input("**bearerToken**",
                                                  value="AAAAAAAAAAAAAAAAAAAAAO5anwEAAAAAAg7Yq3LHcT8GHU9CdUM9Xdnx%2Bpk%3DUw9bVcY62kCdBrMvPLpumrceyWCpDcv8ThyNd5L8ibHRVukxXq",
                                                  key=6)

            apiKey_twitter = kpi3.text_input("**apiKey**", value="rlK5eBq5FiaCjIl1HNQYj8tIl", key=7)

            apiKeySecret_twitter = kpi3.text_input("**apiKeySecret**",
                                                   value="9VCDYva7ymUtFhukFoZJksr2BKoIXm4zFpLbwIym6ikWKEssRH",
                                                   key=8)

            accessToken_twitter = kpi3.text_input("**accessToken**",
                                                  value="1660903613076758528-rGhNMF88anjfG0GpVnpfNYZY9RQl1J", key=9)

            accessTokenSecret_twitter = kpi3.text_input("**accessTokenSecret**",
                                                        value="oy761O8aJqCW1mdfqGBAuak2gULNA5t4NXJhTLLkoNDfK",
                                                        key=10)

        st.form_submit_button("Register")

        # print('PageId_facebook_value', PageId_facebook_value)
        mydict_i.update(
            {'PageId_facebook_value': PageId_facebook_value, 'accessToken_facebook': accessToken_facebook,
             'PageId_linkedin': PageId_linkedin, 'accessToken_linkedin': accessToken_linkedin,
             'bearerToken_twitter': bearerToken_twitter,
             'apiKey_twitter': apiKey_twitter, 'apiKeySecret_twitter': apiKeySecret_twitter,
             'accessToken_twitter': accessToken_twitter,
             'accessTokenSecret_twitter': accessTokenSecret_twitter})

        return mydict_i
