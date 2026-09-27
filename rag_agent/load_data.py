from langchain_community.document_loaders import TextLoader
from langchain_core.documents import Document

# Load data
loader = TextLoader("akgec_courses.txt", encoding="utf-8")
documents = loader.load()

text = documents[0].page_content

# Split using separator between course records
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

for i, chunk in enumerate(chunks, start=1):
    print(f"\n--- Chunk {i} ---")
    print(chunk.page_content)