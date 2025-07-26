from pyexpat import model
from llama_index.core import (
    VectorStoreIndex,
    StorageContext,
    load_index_from_storage,
    settings
)

from QAWithPDF.data_ingestion import load_data
from llama_index.embeddings.google_genai import GoogleGenAIEmbedding

import sys
from exceptions import customexception
from logger import logging

def download_embeddings(model, document):
    """
    Downloads the embeddings for the QA system.
    """

    settings.llm = model
    settings.embed_model = GoogleGenAIEmbedding(model="models/embedding-001")
    settings.chunk_size = 800  # Setting the chunk size for processing 
    settings.chunk_overlap = 100  # Setting the overlap size for chunks

    # Create an index with GoogleGenAI embeddings
    index = VectorStoreIndex.from_documents(
        document,
        embed_model=settings.embed_model,
        llm=settings.llm,
    )

    # Save the index to storage
    index.storage_context.persist(persist_dir="./storage")
    
    logging.info("Embeddings downloaded and stored successfully.")
    return index.as_query_engine(llm=settings.llm)