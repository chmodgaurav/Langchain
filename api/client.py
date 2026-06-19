import streamlit as st
import requests


def get_ollama_response(input_text):
    response = requests.post(
        "http://localhost:8000/predict/invoke",
        json={"input": {"question": input_text}}
    )
    return response.json()["output"]["content"]


#streamlt framework
st.title("LangChain API Client")
input_text=st.text_input("Enter your question:")

if input_text:
    st.write(get_ollama_response(input_text))