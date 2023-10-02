import json
import os

import streamlit as st

from utils.utils import load_post, post_info, convert_unix_to_utc, text_formatting, get_page_info


def run():
    # creating a single-element container
    placeholder = st.empty()
    with placeholder.container():
        # create three columns
        kpi1, kpi2, kpi3 = st.columns(3)

        with kpi1.container():

            kpi1.image(
                "https://upload.wikimedia.org/wikipedia/en/thumb/0/04/Facebook_f_logo_%282021%29.svg/2048px-Facebook_f_logo_%282021%29.svg.png",
                width=50)

            try:

                facebook_info = {}
                data = get_page_info(os.getenv('url'), st.session_state.register_id)

                for value in (data['faceBook']['accounts']['data']):
                    facebook_info[value['name']] = value['id']

                option = kpi1.radio(
                    '**Select the Page**',
                    facebook_info.keys())

                faceBook_post_id = facebook_info[option]
                # print('faceBook_post_app_id', faceBook_post_app_id)

                registration_id = st.session_state.register_id

                facebook_response = load_post(os.getenv('url'), registration_id, 'faceBook', faceBook_post_id)

                # Initialize a dictionary to store Facebook post details
                facebook_post_details = {}

                # Initialize variables to store temporary data for each post
                post_time = None

                # Loop through each item in 'facebook_response'
                for i in facebook_response['posts']['data']:
                    post_time = i['created_time']
                    message = i['message']
                    post_id = i['id']

                    post_details = {
                        'PostTime': post_time,
                        'Message': message,
                        'Post_ID': post_id
                    }

                    # Use the 'Post_ID' as the key to store the post_details dictionary in the main dictionary
                    facebook_post_details[post_id] = post_details

                # print('facebook_post', facebook_post_details)
                option = kpi1.selectbox('select the post', facebook_post_details.keys())
                kpi1.markdown(
                    f'<p class="text_border"><b>Message : </b>{facebook_post_details[option]["Message"]} <br />  <b>Post_ID : </b>{facebook_post_details[option]["Post_ID"]} <br /> <b>Post Time : </b>{facebook_post_details[option]["PostTime"]}</p>',
                    unsafe_allow_html=True)
                # print(os.getenv('url'))
                post_information = post_info(os.getenv('url'), registration_id, 'faceBook',
                                             facebook_post_details[option]["Post_ID"])

                if 'comments' in post_information:
                    for j in post_information['comments']['data']:
                        kpi1.markdown(
                            f'<p class="text_border"><b>comments : </b>{j["message"]} <br /> <b> Person Name: </b> {j["from"]["name"]} <br /> <b> Time : </b> {j["created_time"]}',
                            unsafe_allow_html=True)

                # kpi1.json(post_information)
            except:
                kpi1.write('Data has been not formatted')

        with kpi2.container():

            kpi2.image(
                "https://static-00.iconduck.com/assets.00/linkedin-icon-2048x2048-ya5g47j2.png",
                width=50)
            try:

                registration_id = st.session_state.register_id

                response = load_post(os.getenv('url'), registration_id, 'linkedIn', 'linkedIn_post_app_id')

                linekdIn_response = json.dumps(response['postList'])
                linekdIn_response = linekdIn_response.replace("'", '')
                linekdIn_response = linekdIn_response.replace('"{', '')
                linekdIn_response = linekdIn_response.split(',')

                for index, i in enumerate(linekdIn_response):

                    if 'id: urn:li:share:' in i:

                        id = i.split('id: urn:li:share:')
                        page_id = id[-1]
                        # kpi2.write(f'**Page ID:** {page_id}', key=2121)
                    elif 'createdAt:' in i:
                        date_time = i.split('createdAt:')
                        utc_time = convert_unix_to_utc(int(date_time[-1]))
                        # print("UTC Time:", utc_time)
                        # kpi2.write(f'**Post Time:** {utc_time}', key=21211)

                    elif 'commentary' in i:
                        data = i.split('commentary: ')
                        post_data_new = data[-1]
                        text_formatting(kpi2)
                        # kpi2.markdown(
                        #     f'<p class="text_border"><b>Post Data : </b>{post_data_new}</p>',
                        #     unsafe_allow_html=True)

            except:
                kpi2.write('Fix the Registration Error')
        #
        # with kpi3.container():
        #     kpi3.image(
        #         "https://png.pngtree.com/png-vector/20221018/ourmid/pngtree-twitter-social-media-round-icon-png-image_6315985.png",
        #         width=50)
        #
        #     try:
        #         # data = get_page_info(os.getenv('url'), st.session_state.register_id)
        #         # print('data', data)
        #         kpi3.write("**Error**: End Points are not available", key='000')

        # except:
        #     kpi3.write('Fix the Registration Error')

    if st.button('Create Post'):
        st.session_state['count'] += 1
        st.session_state.fetch_button = 9
