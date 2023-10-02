import os

import streamlit as st
from utils.utils import get_page_info, text_formatting


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
                data = get_page_info(os.getenv('url'), st.session_state.register_id)

                for index, value in enumerate(data['faceBook']['accounts']['data']):
                    text_formatting(kpi1)
                    kpi1.markdown(
                        f'<p class="text_border"><b>Page Name : </b>{value["name"]} <br />  <b>PageId : </b>{value["id"]} <br />  <b>Followers : </b>{value["followers_count"]}  <br />  <b>Category : </b>{value["category"]} </p>',
                        unsafe_allow_html=True)

                    # print('PageId', value['id'])
                    # All_post = load_post(os.getenv('url'), st.session_state.register_id, 'faceBook', value['id'])
                    # kpi1.json(All_post)

            except:
                kpi1.write('Fix the Registration Error')

        with kpi2.container():

            kpi2.image(
                "https://static-00.iconduck.com/assets.00/linkedin-icon-2048x2048-ya5g47j2.png",
                width=50)
            try:
                data = get_page_info(os.getenv('url'), st.session_state.register_id)
                # print('data', data)

                text_formatting(kpi2)
                kpi2.markdown(
                    f'<p class="text_border"><b>User Name : </b>{data["linkedIn"]["vanityName"]} <br />  <b>User ID : </b>{data["linkedIn"]["id"]}</p>',
                    unsafe_allow_html=True)

                # All_post = load_post(os.getenv('url'), st.session_state.register_id, 'linkedIn', 'id')
                # kpi3.json(All_post)
            except:
                kpi2.write('Fix the Registration Error')

        with kpi3.container():
            kpi3.image(
                "https://png.pngtree.com/png-vector/20221018/ourmid/pngtree-twitter-social-media-round-icon-png-image_6315985.png",
                width=50)

            try:
                data = get_page_info(os.getenv('url'), st.session_state.register_id)
                # print('data', data)
                # print(data["twitter"]['data']['username'])

                text_formatting(kpi3)
                kpi3.markdown(
                    f'<p class="text_border"><b>Name : </b>{data["twitter"]["data"]["name"]} <br />  <b>User Name : </b> {data["twitter"]["data"]["username"]}</p>',
                    unsafe_allow_html=True)

                # All_post = load_post(os.getenv('url'), st.session_state.register_id, 'twitter', 'id')
                # kpi3.json(All_post)
            except:
                kpi3.write('Fix the Registration Error')

    if kpi3.button('Get Page Post', 14):

        st.session_state['count'] += 1
