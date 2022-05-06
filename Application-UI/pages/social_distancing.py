import streamlit as st
import webbrowser
from PIL import Image


def app():
    st.title('Social Distancing Visualizer')
    image = Image.open('social-distancing.png')
    col1, col2, col3,col4,col5 = st.columns([2,2, 7, 5,5])
    col3.image(image, use_column_width=True)
   
    url = 'https://riteshsharma-nitk.github.io/social-distancing-ui.github.io/'
    if st.button('Visualize'):
        webbrowser.open_new_tab(url)