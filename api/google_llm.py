from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from fastapi import FastAPI
from langserve import add_routes
import os
import uvicorn
from dotenv import load_dotenv

load_dotenv()
os.environ["GEMINI_API_KEY"]=os.getenv("GEMINI_API_KEY")

##Langsmith Tracking
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"] = "true"

app=FastAPI(
    title="GooGle Server",
    version="1.0",
    description="A server for Google Gemini models.",
)

model=ChatGoogleGenerativeAI(model="gemini-2.5-flash")

prompt=ChatPromptTemplate.from_template("You are an expert in everything. Answer the question: {question}")

add_routes(
    app,
    prompt | model,
    path="/predict"
)

if __name__=="__main__":
    uvicorn.run(app,host="localhost",port=8000)