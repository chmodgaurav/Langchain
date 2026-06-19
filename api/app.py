from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate
from fastapi import FastAPI
from langserve import add_routes
import os
import uvicorn
from dotenv import load_dotenv

load_dotenv()

##Langsmith Tracking
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"] = "true"

app = FastAPI(
    title="Langchain Server",
    version="1.0",
    description="A server for Langchain agents using Ollama models.",
)


llm=ChatOllama(model=os.getenv("OLLAMA_MODEL"))

prompt=ChatPromptTemplate.from_template("You are an expert in everything. Answer the question: {question}")


add_routes(
    app,
    prompt|llm,
    path="/predict"
)

if __name__=="__main__":
    uvicorn.run(app,host="localhost",port=8000)
