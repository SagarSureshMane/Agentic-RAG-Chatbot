from langchain_chroma import Chroma
from langchain_community.vectorstores.chroma import Chroma
from langchain_openai import OpenAIEmbeddings

def get_retriever():
    embeddings = OpenAIEmbeddings()

    vectorcb = Chroma(
        persist_directory="chroma_db",
        embedding_function=embeddings
    )

    return vectorcb.as_retriever(
        search_kwargs ={"k":4}
    )