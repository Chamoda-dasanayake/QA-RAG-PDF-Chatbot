import sys

def check_imports():
    output = []
    try:
        output.append("Attempting imports...")
        
        try:
            from langchain_community.document_loaders import UnstructuredPDFLoader
            output.append("SUCCESS: langchain_community.document_loaders.UnstructuredPDFLoader")
        except ImportError as e:
            output.append(f"FAIL: langchain_community.document_loaders.UnstructuredPDFLoader - {e}")

        try:
            from langchain_text_splitters import RecursiveCharacterTextSplitter
            output.append("SUCCESS: langchain_text_splitters.RecursiveCharacterTextSplitter")
        except ImportError as e:
            output.append(f"FAIL: langchain_text_splitters.RecursiveCharacterTextSplitter - {e}")

        try:
            from langchain_huggingface import HuggingFaceEmbeddings
            output.append("SUCCESS: langchain_huggingface.HuggingFaceEmbeddings")
        except ImportError as e:
            output.append(f"FAIL: langchain_huggingface.HuggingFaceEmbeddings - {e}")

        try:
            from langchain_chroma import Chroma
            output.append("SUCCESS: langchain_chroma.Chroma")
        except ImportError as e:
            output.append(f"FAIL: langchain_chroma.Chroma - {e}")

        try:
            from langchain_groq import ChatGroq
            output.append("SUCCESS: langchain_groq.ChatGroq")
        except ImportError as e:
            output.append(f"FAIL: langchain_groq.ChatGroq - {e}")

        try:
            from langchain.chains import RetrievalQA
            output.append("SUCCESS: langchain.chains.RetrievalQA")
        except ImportError as e:
            output.append(f"FAIL: langchain.chains.RetrievalQA - {e}")

    except Exception as e:
        output.append(f"GENERAL ERROR: {e}")
    
    with open("check_imports_result.txt", "w") as f:
        f.write("\n".join(output))
    print("\n".join(output))

if __name__ == "__main__":
    check_imports()
