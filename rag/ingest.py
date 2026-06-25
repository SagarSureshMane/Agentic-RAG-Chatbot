from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_chroma import Chroma
from rag.loaders import load_document

def ingest_document(path):

    docs = load_document(path)

    print("Documents Loaded:", len(docs))

    # Check extracted text
    for i, doc in enumerate(docs[:3]):
        print(f"\nDocument {i+1}")
        print("Length:", len(doc.page_content))
        print(doc.page_content[:300])

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200
    )

    chunks = splitter.split_documents(docs)

    print("Chunks Created:", len(chunks))

    if len(chunks) == 0:
        raise Exception("No chunks created")

    print("\nFirst Chunk:")
    print(chunks[0].page_content[:500])

    embeddings = OpenAIEmbeddings()

    # Test embedding directly
    test_embedding = embeddings.embed_query("Hello World")
    print("Embedding Length:", len(test_embedding))

    vectordb = Chroma(
        persist_directory="chroma_db",
        embedding_function=embeddings
    )

    vectordb.add_documents(chunks)

    print("Documents added successfully")

    return True