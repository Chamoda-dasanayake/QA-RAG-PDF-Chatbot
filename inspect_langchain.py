import langchain
import os

print(f"Langchain version: {langchain.__version__}")
print(f"Langchain file: {langchain.__file__}")
if hasattr(langchain, '__path__'):
    print(f"Langchain path: {langchain.__path__}")

try:
    import langchain.chains
    print("langchain.chains imported successfully")
except ImportError as e:
    print(f"Failed to import langchain.chains: {e}")

try:
    from langchain.chains import RetrievalQA
    print("RetrievalQA imported successfully")
except ImportError as e:
    print(f"Failed to import RetrievalQA: {e}")
