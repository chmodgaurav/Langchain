from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

import streamlit as st
import os
from dotenv import load_dotenv

load_dotenv()

##Calling Environment Variables
os.environ["Ollama_Model"] = os.getenv("OLLAMA_MODEL")

##Langsmith Tracking
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"] = "true"

##creating Chatbot

prompt = ChatPromptTemplate.from_messages([
    ("system","You are a HelpFull Assistant. Please Provide response to the user query in a concise manner."),
    ("user","Question: {question}")
])

##Streamlit Framework
st.title("Langchain Demo With Ollama")
input_text=st.text_input("Enter your question here:")

##Ollama calling
llm=ChatOllama(model="gemma3:4b", temperature=0.7)
output_parser=StrOutputParser()

##chain
chain=prompt | llm | output_parser

if input_text:
    st.write(chain.invoke({"question":input_text}))

