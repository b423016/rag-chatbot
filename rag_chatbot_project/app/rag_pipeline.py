from langchain.vectorstores import FAISS
from langchain.embeddings import OpenAIEmbeddings
from langchain.llms import OpenAI
import pandas as pd
import os
from dotenv import load_dotenv
import time
from openai import OpenAIError

# Load environment variables from .env file
load_dotenv()

def setup_rag_pipeline(data: pd.DataFrame):
    """
    Setting up the RAG pipeline using LangChain.
    :param_data: dataFrame containing the data.
    :return: RAG pipeline object.
    """
    openai_api_key = os.getenv("OPENAI_API_KEY")
    if not openai_api_key:
        raise ValueError("OpenAI API key not found in environment variables.")

    # embeddings
    texts = data['content'].tolist()
    embeddings = None
    for _ in range(3):  # Retry up to 3 times
        try:
            embeddings = OpenAIEmbeddings(api_key=openai_api_key).embed_documents(texts)
            break
        except OpenAIError as e:
            if "Rate limit" in str(e):
                print("Rate limit exceeded. Retrying in 10 seconds...")
                time.sleep(10)
            else:
                raise e
    if embeddings is None:
        raise Exception("Failed to embed documents due to rate limit.")

    # Setup vector store
    vector_store = FAISS.from_embeddings(embeddings, texts)

    # Setup LLM with retrieval
    llm = OpenAI(api_key=openai_api_key)
    rag_pipeline = llm.chain_with_retrieval(vector_store)
    
    return rag_pipeline
