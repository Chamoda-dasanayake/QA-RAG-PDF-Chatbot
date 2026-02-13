import os
import sys

# Add current directory to path
sys.path.append(os.getcwd())

from rag_utility import answer_question, process_document_to_chroma_db

print("DEBUG: Starting independent QA test...")
query = "What is the summary of the document?"
print(f"DEBUG: Asking: {query}")

try:
    answer = answer_question(query)
    print(f"DEBUG: Answer Result: {answer}")
except Exception as e:
    print(f"DEBUG: Exception during test: {e}")
