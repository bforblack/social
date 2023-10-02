import os

import streamlit as st

from utils.utils import get_page_info, post_data


def run():
    with st.form("my_form"):

        # create three columns
        kpi1, kpi2, kpi3 = st.columns(3)

        with kpi1.container():
            kpi1.image(
                "https://upload.wikimedia.org/wikipedia/en/thumb/0/04/Facebook_f_logo_%282021%29.svg/2048px-Facebook_f_logo_%282021%29.svg.png",
                width=50)

            try:
                Facebook_Post_data = kpi1.text_input("**Message**", key=15)

                face_book_info = {}
                data = get_page_info(os.getenv('url'), st.session_state.register_id)
                for value in (data['faceBook']['accounts']['data']):
                    face_book_info[value['name']] = value['id']

                option = kpi1.selectbox(
                    '**Select the Page ID**',
                    face_book_info.keys())

                faceBook_post_app_id = face_book_info[option]
                # print('faceBook_post_app_id', faceBook_post_app_id)
            except:
                kpi1.write('Check facebook Registration')

        with kpi2.container():
            kpi2.image(
                "https://static-00.iconduck.com/assets.00/linkedin-icon-2048x2048-ya5g47j2.png",
                width=50)
            Linkedin_Post_data = kpi2.text_input("**Message**", key=17)

        with kpi3.container():
            kpi3.image(
                "https://png.pngtree.com/png-vector/20221018/ourmid/pngtree-twitter-social-media-round-icon-png-image_6315985.png",
                width=50)
            Twitter_Post_message = kpi3.text_input("**Message**", key=19)

        if st.form_submit_button("Submit Post"):
            try:
                insert_id = st.session_state.data_id
                # print('insert_id', insert_id)
                registration_id = st.session_state.register_id

                # print(faceBook_post_app_id, registration_id, Facebook_Post_data)

                response = post_data(os.getenv('url'), faceBook_post_app_id, registration_id, Facebook_Post_data,
                                     'faceBook')
                # print('new',response)
                kpi1.write(f"**Post_ID :** {response}")
                kpi1.write(f"**Message :** {Facebook_Post_data}")

                response = post_data(os.getenv('url'), 'linedIn_id', registration_id, Linkedin_Post_data,
                                     'linkedIn')
                kpi2.write(f"**Post_ID :** {response}")
                kpi2.write(f"**Message :** {Linkedin_Post_data}")

                response = post_data(os.getenv('url'), 'twitter_id', registration_id, Twitter_Post_message,
                                     'twitter')
                kpi3.write(f"**Post_ID :** {response}")
                kpi3.write(f"**Message :** {Twitter_Post_message}")
            except:
                kpi2.write('Check Registration')

            st.session_state['count'] += 1
    if st.button('Next Page'):
        st.session_state.fetch_button = 9
