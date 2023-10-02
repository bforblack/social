import base64
import json
import os
from pathlib import Path

import requests
import streamlit as st
import datetime

from dotenv import load_dotenv
from logs.logger import Logger

logger = Logger()
config_path = os.path.join('config', 'config.env')


def img_base64(img_path):
    """
    :param img_path: image path
    :return: encoded image
    """
    try:
        img_bytes = Path(img_path).read_bytes()
        encoded = base64.b64encode(img_bytes).decode()
        return encoded
    except Exception as e:
        logger.error_msg(f'encoding failed {e}')


def make_grid(rows, cols):
    """
    :param rows: rows of streamlit
    :param cols: columns of streamlit    :return:  grid
    """
    try:
        grid = [0] * rows
        for i in range(rows):
            with st.container():
                grid[i] = st.columns(cols)
        return grid
    except Exception as e:
        logger.error_msg(f'grid creation failed {e}')


def load_environ():
    try:
        environment = load_dotenv(dotenv_path=config_path)
        logger.info_msg('Environment is loaded')
        return environment
    except Exception as ex:
        logger.error_msg(f'{ex}')
        raise


def fetch_data(url, payload):
    # [(key_name, value)]
    """
    :param url: url address aadhaar or pan card extraction api url
    :param payload: list of key, value pair tuple
    :return:
    """
    with st.spinner('Wait for data fetching'):
        try:
            data = {}
            for i in payload:
                data.update({i[0]: i[1]})

            # Send the request to the endpoint
            response = requests.post(url, json=data)

            return response.json()
        except Exception as Ex:
            # print("error", Ex)
            return {}


def post_data(url, pageId, registration_id, message, media_source):
    # [(key_name, value)]
    """
    :param message:
    :param url: url address aadhaar or pan card extraction api url
    :return:
    """
    with st.spinner('Wait for Post Data'):
        try:
            url = url + "/create/" + registration_id

            payload = json.dumps({
                "pageId": pageId,
                "data": message,
                "mediaSource": media_source
            })
            response = requests.request("POST", url, data=payload)

            return response.json()
        except Exception as Ex:
            # print("error", Ex)
            return {}


def dict_empty(my_dict):
    out_put = []
    for value in my_dict.values():
        if value == '':
            out_put.append(False)
        else:
            out_put.append(True)
    return any(out_put)





def register(url, mydict_i):
    facebook_appId=mydict_i['PageId_facebook_value']
    face_token_id=mydict_i['accessToken_facebook']
    instagram_appid="instagram_appid"
    instagram_token_id="instagram_token_id"
    twitter_bearerToken=mydict_i['bearerToken_twitter']
    twitter_apiKey=mydict_i['apiKey_twitter']
    twitter_apiKeySecret=mydict_i['apiKeySecret_twitter']
    twitter_accessToken=mydict_i['accessToken_twitter']
    twitter_accessTokenSecret=mydict_i['accessTokenSecret_twitter']
    linkedIn_appId=mydict_i['PageId_linkedin']
    linkedIn_accessToken=mydict_i['accessToken_linkedin']
    with st.spinner('Wait for Registration'):
        try:
            registrationId = "c3b6c077-d57b-4f94-8023-aad251d351b5"
            url = url + "/register/"

            payload = json.dumps({
                "_id": "123",
                "username": "Businessnext",
                "registrationId": registrationId,
                "faceBook": {
                    "appId": facebook_appId,
                    "accessToken": face_token_id
                },
                "instagram": {
                    "appId": instagram_appid,
                    "accessToken": instagram_token_id
                },
                "twitter": {
                    "bearerToken": twitter_bearerToken,
                    "apiKey": twitter_apiKey,
                    "apiKeySecret": twitter_apiKeySecret,
                    "accessToken": twitter_accessToken,
                    "accessTokenSecret": twitter_accessTokenSecret
                },
                "linkedIn": {
                    "appId": linkedIn_appId,
                    "accessToken": linkedIn_accessToken
                }
            })

            response = requests.request("POST", url, data=payload)

            return response.json()
        except Exception as Ex:
            # print("error", Ex)
            return {}

        # print(response.text)


def get_page_info(url, registration_id):
    # print(registration_id)
    with st.spinner('Wait for Page Information'):
        try:
            url = url + "/" + registration_id

            response = requests.request("GET", url)
            return response.json()
        except Exception as Ex:
            # print("error", Ex)
            return {}


def load_post(url, registration_id, media_source, page_id):
    with st.spinner('Wait for Post Fetch'):
        try:
            url = url + "/posts/" + registration_id
            payload = json.dumps({
                "mediaSource": media_source,
                "pageId": page_id
            })

            response = requests.request("GET", url, data=payload)
            return response.json()
        except Exception as Ex:
            # print("error", Ex)
            return {}


def text_formatting(container):
    """
    :param container: streamlit container , which you want to formate
    :return: -
    """
    container.markdown("""<style> .text_border {border-radius: 10px;
      border: 1px solid black;
      width: 250px;
      padding: 2px;
      text-align: left;
      margin-left: 2px;} </style> 
                                """, unsafe_allow_html=True)


def convert_unix_to_utc(timestamp):
    # Convert Unix timestamp to datetime object
    utc_datetime = datetime.datetime.utcfromtimestamp(timestamp / 1000.0)

    # Format datetime object as string
    utc_string = utc_datetime.strftime('%Y-%m-%d %H:%M:%S')

    return utc_string


def post_info(url, registration_id, media_source, post_id):
    # print(url, registration_id, media_source, post_id)
    with st.spinner('Wait for Post Information'):
        try:
            url = url + "/posts/" + registration_id
            payload = json.dumps({
                "mediaSource": str(media_source),
                "postId": str(post_id)
            })

            response = requests.request("GET", url, data=payload)
            return response.json()
        except Exception as Ex:
            # print("error", Ex)
            return {}
