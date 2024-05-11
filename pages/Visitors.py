import streamlit as st
from PIL import Image
st.write("<h3> Takes Picture and convert & display Greyscale Image.</h3>",unsafe_allow_html=True)
with st.expander("Start Camera"):
    camera_image = st.camera_input("Visitors Photo")

if camera_image:
    img = Image.open(camera_image)
    grey_img = img.convert('L')
    st.image(grey_img)

