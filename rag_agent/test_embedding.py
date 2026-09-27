from sentence_transformers import SentenceTransformer

# Load embedding model
model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

text = "Computer Science and Engineering at AKGEC"

# Convert text into embedding
embedding = model.encode(text)

print("Embedding created successfully!")
print("Embedding dimensions:", len(embedding))
print("First 10 values:", embedding[:10])