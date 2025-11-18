from dotenv import load_dotenv
load_dotenv()
import os
import json
import requests
from uuid import uuid4

from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_core.documents import Document

import faiss
from langchain_community.docstore.in_memory import InMemoryDocstore