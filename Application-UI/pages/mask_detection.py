import streamlit as st
import webbrowser
from PIL import Image


def app():
    st.title('Mask Detection Visualizer')
    image = Image.open('protection-mask.png')
    col1, col2, col3,col4,col5 = st.columns([2,2, 7, 5,5])
    col3.image(image, use_column_width=True)
    url = 'https://riteshsharma-nitk.github.io/mask-detection-ui.github.io/'
    if st.button('Visualize'):
        webbrowser.open_new_tab(url)