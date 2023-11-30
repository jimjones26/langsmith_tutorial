# ------------------------------------------------------------------
# Import Modules
# ------------------------------------------------------------------

import os
import nest_asyncio
import pandas as pd

from dotenv import load_dotenv, find_dotenv
from langsmith import Client
from langchain.chat_models import ChatOpenAI
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.smith import RunEvalConfig, run_on_dataset

nest_asyncio.apply()

# ------------------------------------------------------------------
# Load api keys from .env file
# ------------------------------------------------------------------

load_dotenv(find_dotenv())
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_ENDPOINT"] = "http://api.smith.langchain.com"
os.environ["LANGCHAN_PROJECT"] = "langsmith-tutorial"
