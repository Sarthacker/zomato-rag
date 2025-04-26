import os
from dotenv import load_dotenv
from pinecone import Pinecone
from groq import Groq

load_dotenv()

HUGGING_FACE_MODEL = os.getenv("HUGGING_FACE_MODEL")
LLAMA_MODEL = os.getenv("LLAMA_MODEL")
PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
PINECONE_INDEX = os.getenv("PINECONE_INDEX")
GROQ_API_KEY = os.getenv("GROQ_API_KEY")


pinecone_client = Pinecone(api_key=PINECONE_API_KEY)
index = pinecone_client.Index(PINECONE_INDEX)
client = Groq(api_key=GROQ_API_KEY)