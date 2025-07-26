from llama_index.core import SimpleDirectoryReader
import sys
from exceptions import customexception
from logger import logging

def load_data(data):
    """
    Load PDF documents from the specified path.
    
    Args:
        data (str): The path to the directory containing pdf files.
    
    Returns:
        list: A list of pdf documents loaded from the specified path.

    Raises:
        QAException: If the data path is invalid or if an error occurs during loading.
    """
    try:
        logging.info(f"Loading data from {data}")
        documents = SimpleDirectoryReader("Data").load_data()
        logging.info(f"Successfully loaded {len(documents)} documents.")
        return documents
    except Exception as e:
        logging.error(f"Error loading data from {data}: {e}")
        raise customexception(f"Failed to load data from {data}", sys) from e