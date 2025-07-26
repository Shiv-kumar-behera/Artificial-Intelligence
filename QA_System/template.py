import logging
import os
from pathlib import Path

list_of_files = [
    "QAWithPDF/__init__.py",
    "QAWithPDF/data_ingestion.py",
    "QAWithPDF/embedding.py",
    "QAWithPDF/model_api.py",
    "Experiments/experiments.ipynb",
    "StreamlitApp.py",
    "logger.py",
    "exceptions.py",
    "setup.py",
]

for file in list_of_files:
    file_path = Path(file)
    file_dir, file_name = os.path.split(file_path)
    if file_dir != "":
        os.makedirs(file_dir, exist_ok=True)
        logging.info(f"Created directory: {file_dir}")

    if (not os.path.exists(file_path)) or (os.path.getsize(file_path) == 0):
        with open(file_path, "w") as f:
            pass
            logging.info(f"Created file: {file_path}")

    else:
        logging.info(f"File already exists and is not empty: {file_path}")
