import streamlit as st
# import Image from pillow to open images
from PIL import Image
import base64
from test import add_achievement, view_function

def add_bg_from_local(image_file):
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    st.markdown(
        f"""
    <style>
    .stApp {{
        background-image: url(data:image/{"png"};base64,{encoded_string.decode()});
        background-size: cover
    }}
    </style>
    """,
        unsafe_allow_html=True
    )


add_bg_from_local('BG.jpg')
img = Image.open("logo.png")

col1, col2, col3 = st.columns([1,1,1])

with col1:
    st.write("")

with col2:
    st.image(img, width=200)

with col3:
    st.write("")


st.markdown("<h1 style='text-align: center; color: white;'>  Student Achievement Tracking and Verification </h1>", unsafe_allow_html=True)

st.markdown("<h3 style='text-align: left; color: white;'>  Add Student Achievement </h3>", unsafe_allow_html=True)

description = st.text_input("Enter Your Achievement Description", value = "Type Here ...", key="description")
addr = st.text_input("Enter Your Address",value = "Type Here ...", key="addr")

if st.button("Create Student Achievement"):
    
    result = add_achievement(description, addr)
    st.success("Student Achievement  Added")

st.markdown("<h3 style='text-align: left; color: white;'>  Retrieve Student Achievement </h3>", unsafe_allow_html=True)

addr1 = st.text_input("Enter Student Address to retrieve",value = "Type Here ...", key="addr1")

if st.button("Retrieve Student Achievement"):
    result = view_function(addr1)
    st.success(result)