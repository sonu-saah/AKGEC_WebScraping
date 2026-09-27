from sentence_transformers import SentenceTransformer
from langchain_core.documents import Document

# Load AKGEC data
with open("akgec_courses.txt", "r", encoding="utf-8") as file:
    text = file.read()

# Split into individual course records
records = text.split("--------------------------------------------------")

chunks = []

for record in records:
    record = record.strip()

    if record and "Course:" in record:
        chunks.append(
            Document(
                page_content=record,
                metadata={"source": "akgec_courses.txt"}
            )
        )

print("Total chunks:", len(chunks))

# Load embedding model
model = SentenceTransformer(
    "sentence-transformers/all-MiniLM-L6-v2"
)

# Convert chunks into embeddings
texts = [chunk.page_content for chunk in chunks]

embeddings = model.encode(texts)

print("Embeddings created successfully!")
print("Number of embeddings:", len(embeddings))
print("Embedding dimensions:", len(embeddings[0]))