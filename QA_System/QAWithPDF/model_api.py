import os
from dotenv import load_dotenv
import sys

from llama_index.llms.google_genai import GoogleGenAI
from IPython.display import display, Markdown
import google.generativeai as genai
from exceptions import customexception
from logger import logging

load_dotenv()

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

genai.configure(api_key=GOOGLE_API_KEY)

def load_model():
    """
    Loads the GoogleGenAI model for the QA system.
    """
    try:
        # Initialize the GoogleGenAI model
        model = GoogleGenAI(models="gemini-1.5-pro-latest", api_key=GOOGLE_API_KEY)
        logging.info("Model loaded successfully.")
        return model
    except Exception as e:
        logging.error(f"Error loading model: {e}")
        raise customexception("Failed to load model.", sys) from e