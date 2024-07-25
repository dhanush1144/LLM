import streamlit as st
import os
import textwrap

import google.generativeai as genai

from IPython.display import display
from IPython.display import Markdown


def to_markdown(text):
    text = text.replace('•', '  *')
    return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))

# Directly set the API key
api_key = " "  # Replace with your actual API key
genai.configure(api_key=api_key)

# Function to load the generative model and get responses
def get_gemini_response(question):
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(question)
    return response.text

# Initialize our Streamlit app
st.set_page_config(page_title="Q&A Demo")
st.header("Gemini Application")

input = st.text_input("Input: ", key="input")
submit = st.button("Ask the question")

if submit:
    response = get_gemini_response(input)
    st.subheader("The Response is")
    st.write(response)
