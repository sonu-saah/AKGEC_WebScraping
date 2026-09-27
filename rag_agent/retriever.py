from sentence_transformers import SentenceTransformer
from langchain_chroma import Chroma


# Load embedding model
model = SentenceTransformer(
    "sentence-transformers/all-MiniLM-L6-v2"
)


# Function to create embedding
def embed_query(text):
    return model.encode(text).tolist()


# Connect to existing Chroma database
vector_db = Chroma(
    collection_name="akgec_courses",
    persist_directory="./chroma_db"
)


# User question
question = "How many seats are available in Computer Science and Engineering?"


# Convert question into embedding
query_embedding = embed_query(question)


# Search similar documents
results = vector_db._collection.query(
    query_embeddings=[query_embedding],
    n_results=3
)


print("\nRelevant chunks:\n")

for i, document in enumerate(results["documents"][0], start=1):
    print(f"--- Result {i} ---")
    print(document)
    print()