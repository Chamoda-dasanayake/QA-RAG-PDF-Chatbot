from langchain.chains import RetrievalQA
from langchain_groq import ChatGroq
from langchain_huggingface import HuggingFaceEmbeddings

print("Imports successful")
try:
    # Just checking if classes are available, not full instantiation which might need API keys
    print(f"RetrievalQA: {RetrievalQA}")
    print(f"ChatGroq: {ChatGroq}")
    print(f"HuggingFaceEmbeddings: {HuggingFaceEmbeddings}")
    print("Classes found")
except Exception as e:
    print(f"Error: {e}")
