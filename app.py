import os
import streamlit as st

st.write("Debug: App starting...")
try:
    from rag_utility import process_document_to_chroma_db, answer_question
    st.write("Debug: rag_utility imported successfully.")
except Exception as e:
    st.error(f"Error importing rag_utility: {e}")
  

working_dir = os.getcwd()

st.title("Llama-3.3-70B - Document RAG")
uploaded_file = st.file_uploader("Upload a PDF document", type=["pdf"]) 

if uploaded_file is not None:
    save_path = os.path.join(working_dir, uploaded_file.name)
    with open(save_path, "wb") as f:
        f.write(uploaded_file.getbuffer())
    
    process_document = process_document_to_chroma_db(uploaded_file.name)
    st.info("Document uploaded successfully")

user_question = st.text_input("Enter your question about the document:")    

if st.button("Get Answer"):
    answer = answer_question(user_question)

    st.markdown("###Llama-3.3-70B Response:")
    st.write(answer)