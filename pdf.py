from dotenv import load_dotenv
load_dotenv()
import streamlit as st
import os
from PIL import Image
import fitz  # PyMuPDF
import google.generativeai as genai

api_key = "AIzaSyBepBOJ-St1LnQ2Gws8c869uNrKgJxC8tI" 
genai.configure(api_key=api_key)
model = genai.GenerativeModel('gemini-pro')
input="based on the document provide a score out of 100 for the faculty and an analysis of the document uploaded, for the role of associate professor in the department of computer science and engineering"

def get_gemini_response(input, content):
    if input:
        response = model.generate_content([input, content])
    else:
        response = model.generate_content(content)
    return response.text

def extract_text_from_pdf(file):
    pdf_document = fitz.open(stream=file.read(), filetype="pdf")
    text = ""
    for page_num in range(pdf_document.page_count):
        page = pdf_document.load_page(page_num)
        text += page.get_text()
    return text

st.set_page_config(page_title="Panimalar Analysis Platform")
st.header("Analyze Faculty Document")
uploaded_file = st.file_uploader("Choose a file...", type=["pdf"])

content = ""
if uploaded_file is not None:
    if uploaded_file.type == "application/pdf":
        content = extract_text_from_pdf(uploaded_file)
        st.write("PDF content extracted.")
    else:
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Image.", use_column_width=True)
        content = image  # For images, we pass the image object directly

submit = st.button("Generate Score")

if submit:
    response = get_gemini_response(input, content)
    st.subheader("The Response is")
    st.write(response)
