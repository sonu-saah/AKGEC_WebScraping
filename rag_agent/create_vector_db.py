from sentence_transformers import SentenceTransformer
from langchain_chroma import Chroma
from langchain_core.documents import Document


# 1. Load AKGEC data
with open("akgec_courses.txt", "r", encoding="utf-8") as file:
    text = file.read()


# 2. Create individual course chunks
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


# 3. Load embedding model
model = SentenceTransformer(
    "sentence-transformers/all-MiniLM-L6-v2"
)


# 4. Create embeddings
texts = [chunk.page_content for chunk in chunks]
embeddings = model.encode(texts)


# 5. Create Chroma database
vector_db = Chroma(
    collection_name="akgec_courses",
    embedding_function=None,
    persist_directory="./chroma_db"
)


# 6. Add documents and embeddings
vector_db._collection.add(
    ids=[str(i) for i in range(len(chunks))],
    documents=texts,
    embeddings=embeddings.tolist(),
    metadatas=[chunk.metadata for chunk in chunks]
)


print("Vector database created successfully!")
print("Location: ./chroma_db")