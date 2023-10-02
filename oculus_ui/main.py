import os

import streamlit as st
from PIL import Image
import time
import base64
from utils.utils import load_environ, img_base64, register, dict_empty
from paging import page_1, page_3, page_4, page_5
from paging import page_2
from logs.logger import Logger

_logger = Logger()
load_environ()

now = time.time()

# page formatting

icon_img = Image.open('ui_template/CRMNEXT_Logo.png')
st.set_page_config(page_title='Data Next Preprod', page_icon=icon_img, layout='wide')
# logo
header_html = """<p><img align='right' src='data:image/png;base64,{}' class='img-fluid'style='width:128px;height:128px; margin-top: 25px;
  margin-right: 25px'></p>""".format(
    img_base64("ui_template/logo.jpeg")
)
st.markdown(
    header_html, unsafe_allow_html=True,
)
# menu button hide
hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)
# page styling
with open('ui_template/style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

# '''-------page session--------'''
if 'count' not in st.session_state:
    st.session_state['count'] = 0

if 'fetch_button' not in st.session_state:
    st.session_state.fetch_button = 0

# '''----------Database Id session----------------'''
if 'data_id' not in st.session_state:
    st.session_state.data_id = 0
# '''----------widget_key Id session----------------'''
if 'widget_key' not in st.session_state:
    st.session_state.widget_key = 0
# input key
if 'input_key' not in st.session_state:
    st.session_state.input_key = 0
# register session
if 'register_id' not in st.session_state:
    st.session_state.register_id = 0


def main():
    # page 1
    if st.session_state['count'] == 0:
        st.markdown(
            f'<h1 style="text-align: center;font-size:36px;">{"Social Next"}</h1>', unsafe_allow_html=True)
        st.subheader("Registration")

        mydict_i = page_1.run()

        if dict_empty(mydict_i):
            register_id = register(os.getenv('url'), mydict_i)
            st.session_state['register_id'] = register_id

            st.session_state['count'] += 1


    # page 2
    elif st.session_state['count'] == 1:
        st.markdown(
            f'<h1 style="text-align: center;font-size:36px;">{"Social Page Info"}</h1>', unsafe_allow_html=True)

        page_2.run()

        # page 3
    elif st.session_state['count'] == 2:
        st.markdown(
            f'<h1 style="text-align: center;font-size:36px;">{"Social Post Info"}</h1>', unsafe_allow_html=True)
        page_3.run()




    # page 4
    elif st.session_state['count'] == 3:
        st.markdown(
            f'<h1 style="text-align: center;font-size:36px;">{"Post Info"}</h1>', unsafe_allow_html=True)
        page_4.run()






    # page 5
    elif st.session_state['count'] == 4:
        st.markdown(
            f'<h1 style="text-align: center;font-size:36px;">{"Create Post"}</h1>', unsafe_allow_html=True)

        page_5.run()

    elif st.session_state['count'] == 5:

        st.markdown(
            f'<h1 style="text-align: center;font-size:36px;">{"Social Analytics"}</h1>', unsafe_allow_html=True)

        def show_pdf(file_path):
            with open(file_path, "rb") as file:
                base64_pdf = base64.b64encode(file.read()).decode('utf-8')
            pdf_display = f'<iframe src="data:application/pdf;base64,{base64_pdf}" width="1080" height="800" type="application/pdf"></iframe>'
            st.markdown(pdf_display, unsafe_allow_html=True)

        show_pdf('post3.pdf')


if __name__ == "__main__":
    main()
