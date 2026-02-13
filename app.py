import os
import streamlit as st

from rag_utility import process_document_to_chroma_db, answer_question  

working_dir = os.getcwd()

st.title("Document RAG (Llama-3 8B)")
uploaded_file = st.file_uploader("Upload a PDF document", type=["pdf"]) 

if uploaded_file is not None:
    save_path = os.path.join(working_dir, uploaded_file.name)
    with open(save_path, "wb") as f:
        f.write(uploaded_file.getbuffer())
    
    with st.spinner("Processing document..."):
        process_document = process_document_to_chroma_db(uploaded_file.name)
    
    if process_document == 0:
        st.success("Document uploaded and processed successfully")
    else:
        st.error("Failed to process document. Check terminal logs for details.")

user_question = st.text_input("Enter your question about the document:")    

if st.button("Get Answer"):
    with st.spinner("Getting answer..."):
        answer = answer_question(user_question)

    st.markdown("### Response:")
    st.write(answer)