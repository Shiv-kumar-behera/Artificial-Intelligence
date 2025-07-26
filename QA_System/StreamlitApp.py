import streamlit as st
from QAWithPDF.data_ingestion import load_data
from QAWithPDF.embedding import download_embeddings
from QAWithPDF.model_api import load_model

def main():
    st.set_page_config(page_title="QA System with PDF", layout="wide")

    doc = st.file_uploader("Upload PDF Document", type=["pdf"])

    st.header("QA System with PDF")

    user_question = st.text_input("Ask a question about the PDF document:")

    if st.button("Generate Answer"):
        with st.spinner("Processing..."):
            if doc is not None:
                # Load the data from the PDF
                document = load_data(doc)

                model = load_model()

                # Download embeddings
                query_engine = download_embeddings(model, document)

                # Query the model with the user's question
                if not user_question:
                    st.error("Please enter a question.")
                    return
                response = query_engine.query(user_question)
                st.write(response.response)
            else:
                st.error("Please upload a PDF document.")

if __name__ == "__main__":
    main()
# This is the main entry point for the Streamlit app.