import os
from dotenv import load_dotenv

from langchain_community.document_loaders import UnstructuredPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma
from langchain_groq import ChatGroq
from langchain.chains import RetrievalQA

load_dotenv()

working_dir = os.path.dirname(os.path.abspath(__file__))

# Lazy initialization
embedding = None
llm = None

def get_embedding_model():
    global embedding
    if embedding is None:
        embedding = HuggingFaceEmbeddings()
    return embedding

def get_llm():
    global llm
    if llm is None:
        llm = ChatGroq(
            model="llama-3.1-8b-instant",
            temperature=0
        )
    return llm

def process_document_to_chroma_db(file_name):
    print(f"DEBUG: Processing document {file_name}...")
    try:
        loader = UnstructuredPDFLoader(f"{working_dir}/{file_name}")
        documents = loader.load()
        print(f"DEBUG: Loaded {len(documents)} documents.")

        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=2000,
            chunk_overlap=200,
        )

        texts = text_splitter.split_documents(documents)
        print(f"DEBUG: Split into {len(texts)} chunks.")

        print("DEBUG: Creating Vector DB...")
        vector_db = Chroma.from_documents(
            documents=texts,
            embedding=get_embedding_model(),
            persist_directory=f"{working_dir}/doc_vectorestore"
        )
        print("DEBUG: Vector DB created successfully.")
        return 0
    except Exception as e:
        print(f"ERROR in process_document_to_chroma_db: {e}")
        return None

def answer_question(user_question):
    print(f"DEBUG: Answering question: {user_question}")
    try:
        vector_db = Chroma(
            embedding_function=get_embedding_model(),
            persist_directory=f"{working_dir}/doc_vectorestore"
        )
        print("DEBUG: Vector DB loaded.")

        retriever = vector_db.as_retriever()
        print("DEBUG: Retriever created.")

        qa_chain = RetrievalQA.from_chain_type(
            llm=get_llm(),
            chain_type="stuff",
            retriever=retriever,
            return_source_documents=True
        )
        print("DEBUG: QA Chain created. Invoking...")

        response = qa_chain.invoke({"query": user_question})
        print(f"DEBUG: Response received: {response}")
        answer = response["result"]
        
        return answer
    except Exception as e:
        print(f"ERROR in answer_question: {e}")
        return f"Error: {e}"