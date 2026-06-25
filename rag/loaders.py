from langchain_community.document_loaders import (
    PDFPlumberLoader,
    TextLoader,
    Docx2txtLoader
)

from langchain_core.documents import Document

import pandas as pd


def load_document(path):

    if path.endswith(".pdf"):

        loader = PDFPlumberLoader(path)
        return loader.load()

    elif path.endswith(".txt"):

        loader = TextLoader(path)
        return loader.load()

    elif path.endswith(".docx"):

        loader = Docx2txtLoader(path)
        return loader.load()

    elif path.endswith(".xlsx"):

        df = pd.read_excel(path)

        return [
            Document(
                page_content=df.to_string()
            )
        ]

    else:
        raise Exception(
            "Unsupported file type"
        )