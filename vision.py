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
model = genai.GenerativeModel('gemini-2.0-flash')
input="Extract all details from each of these this bills such as bill number ,date, sender address, receiver address, items, price, quantity, and all other details and display them as a table..also provide data in csv format which can then be saved with .csv extension"

def get_gemini_response(input, image):
    if input!= "":
        response = model.generate_content([input, image])
    else:
        response = model.generate_content(image)
    return response.text
    

st.set_page_config(page_title="Bill Analysis")
st.header("Bill Analyser")
# input = st.text_input("Input Prompt: ", key="input")
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image.", use_column_width=True)
    

submit = st.button("Analyse Bill")

if submit :
    response = get_gemini_response(input, image)
    st.subheader("Extracted Content")
    st.write(response)
