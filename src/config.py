import os
from dotenv import load_dotenv
from pinecone import Pinecone
from groq import Groq
import streamlit as st

load_dotenv()

HUGGING_FACE_MODEL = st.secrets["HUGGING_FACE_MODEL"]
LLAMA_MODEL = st.secrets["LLAMA_MODEL"]
PINECONE_API_KEY = st.secrets["PINECONE_API_KEY"]
PINECONE_INDEX = st.secrets["PINECONE_INDEX"]
GROQ_API_KEY = st.secrets["GROQ_API_KEY"]


pinecone_client = Pinecone(api_key=PINECONE_API_KEY)
index = pinecone_client.Index(PINECONE_INDEX)
client = Groq(api_key=GROQ_API_KEY)