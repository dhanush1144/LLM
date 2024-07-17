from dotenv import load_dotenv
load_dotenv()
import streamlit as st
import os
# import textwrap
from PIL import Image
# import io
import google.generativeai as genai


api_key = "AIzaSyBepBOJ-St1LnQ2Gws8c869uNrKgJxC8tI"  # Replace with your actual API key
genai.configure(api_key=api_key)
model = genai.GenerativeModel('gemini-pro-vision')

def get_gemini_response(input, image):
    if input!="":
        response = model.generate_content([input, image])
    else:
        response = model.generate_content(image)
    return response.text
    

st.set_page_config(page_title="Gemini Image Demo")
st.header("Gemini Application")
input = st.text_input("Input Prompt: ", key="input")
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image.", use_column_width=True)
    
    # Convert image to bytes
    # image_bytes = io.BytesIO()
    # image.save(image_bytes, format=image.format)
    # image_bytes = image_bytes.getvalue()

submit = st.button("Tell me about the image")

if submit :
    response = get_gemini_response(input, image)
    st.subheader("The Response is")
    st.write(response)
