import json
import os

import streamlit as st

from utils.utils import convert_unix_to_utc, text_formatting, load_post, get_page_info


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

                face_book_info = {}
                data = get_page_info(os.getenv('url'), st.session_state.register_id)
                for value in (data['faceBook']['accounts']['data']):
                    face_book_info[value['name']] = value['id']

                option = kpi1.radio(
                    '**Select the Page**',
                    face_book_info.keys())

                faceBook_post_app_id = face_book_info[option]
                # print('faceBook_post_app_id', faceBook_post_app_id)

                registration_id = st.session_state.register_id

                response = load_post(os.getenv('url'), registration_id, 'faceBook', faceBook_post_app_id,
                                     )

                # print(response)

                # Loop through each item in 'facebook_response'
                for i in response['posts']['data']:
                    post_time = i['created_time']
                    message_data = i['message']
                    post_id = i['id']

                    kpi1.markdown(
                        f'<p class="text_border"><b>Message : </b>{message_data} <br /> <b>Post Time: </b> {post_time} <br /> <b>Post_ID : </b>{post_id} </p>',
                        unsafe_allow_html=True)


            except:
                kpi1.write('Data has been not formatted')

        with kpi2.container():

            kpi2.image(
                "https://static-00.iconduck.com/assets.00/linkedin-icon-2048x2048-ya5g47j2.png",
                width=50)
            try:

                registration_id = st.session_state.register_id

                response = load_post(os.getenv('url'), registration_id, 'linkedIn', 'linkedIn_post_app_id')

                # print(response)
                linekdIn_response = json.dumps(response['postList'])
                linekdIn_response = linekdIn_response.replace("'", '')
                linekdIn_response = linekdIn_response.replace('"{', '')
                linekdIn_response = linekdIn_response.split(',')

                for index, i in enumerate(linekdIn_response):

                    if 'id: urn:li:share:' in i:

                        id = i.split('id: urn:li:share:')
                        page_id = id[-1]
                        kpi2.write(f'**Page ID:** {page_id}', key=2121)
                    elif 'createdAt:' in i:
                        date_time = i.split('createdAt:')
                        utc_time = convert_unix_to_utc(int(date_time[-1]))
                        # print("UTC Time:", utc_time)
                        kpi2.write(f'**Post Time:** {utc_time}', key=21211)

                    elif 'commentary' in i:
                        data = i.split('commentary: ')
                        post_data_new = data[-1]
                        text_formatting(kpi2)
                        kpi2.markdown(
                            f'<p class="text_border"><b>Post Data : </b>{post_data_new}</p>',
                            unsafe_allow_html=True)

            except:
                kpi2.write('Fix the Registration Error')

        with kpi3.container():
            kpi3.image(
                "https://png.pngtree.com/png-vector/20221018/ourmid/pngtree-twitter-social-media-round-icon-png-image_6315985.png",
                width=50)

            try:
                # data = get_page_info(os.getenv('url'), st.session_state.register_id)
                # print('data', data)
                kpi3.write("**Error**: End Points are not available", key='000')

            except:
                kpi3.write('Fix the Registration Error')

    if st.button('Post Details'):
        st.session_state['count'] += 1
        st.session_state.fetch_button = 9
