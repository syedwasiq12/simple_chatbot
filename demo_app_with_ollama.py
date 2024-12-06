import os
from dotenv import load_dotenv

from langchain_community.llms import Ollama
import streamlit as st
from langchain_core.prompts import ChatPromptTemplate ##to deaign my own prompt
from langchain_core.output_parsers import StrOutputParser


load_dotenv()


##Langsmith tracking
os.environ['LANGCHAIN_API_KEY']=os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_TRACKING_V2"]='true'
os.environ["LANGCHAIN_PROJECT"]=os.getenv("LANGCHAIN_PROJECT")


##Designing prompt template
prompt=ChatPromptTemplate.from_messages(
    [
        ("system","You are a helpful assistant.Please respond to the questions"),
        ("user","Question:{question}")
    ]
)

##streamlit framework
st.title("This is my langchain demo with gemma:2b")
input_text=st.text_input("What question you have in mind")


##ollama gemma2b model
llm=Ollama(model="gemma:2b")
output_parser=StrOutputParser()
chain=prompt|llm|output_parser

if input_text:
    st.write(chain.invoke({"question":input_text})) ##to write the system response in system

    ##whatever i have done can be tracked from lagchain