import langchain
import langchain_core
import langchain_community

print("Checking langchain locations...")
print(f"langchain: {langchain.__path__}")

try:
    import langchain.chains
    print("Imported langchain.chains")
except ImportError:
    print("Cannot import langchain.chains")

# Check if chains are in core or community
print("\nChecking attributes:")
print(f"langchain_core has chains? {'chains' in dir(langchain_core)}")
print(f"langchain_community has chains? {'chains' in dir(langchain_community)}")

# Try to find RetrievalQA or create_retrieval_chain
def find_obj(name, module):
    if hasattr(module, name):
        print(f"Found {name} in {module.__name__}")
        return True
    return False

find_obj("RetrievalQA", langchain)
find_obj("create_retrieval_chain", langchain)

try:
    from langchain.chains import create_retrieval_chain
    print("Found create_retrieval_chain in langchain.chains")
except ImportError:
    print("create_retrieval_chain not in langchain.chains")
