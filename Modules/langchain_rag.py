from langchain_community.document_loaders import (PyPDFLoader)
from langchain.text_splitter import (RecursiveCharacterTextSplitter)

from langchain_community.vectorstores import(Chroma)
import tempfile
from langchain_huggingface import HuggingFaceEmbeddings
import uuid

def build_retriver (uploaded_file):

    #TEMP
    with tempfile.NamedTemporaryFile(
        delete =False,
        suffix =".pdf"
    ) as tmp:
        tmp.write(uploaded_file.read())
        tmp_path = tmp.name

    
    # lOADING PDF
    loader =PyPDFLoader(tmp_path)
    documents = loader.load()

    ## sPLITTER CHUNKING

    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    chunks = splitter.split_documents(documents)
    print(f"chunks count : {len(chunks)}")

    for chunk in chunks :
        print(f"chunk : {chunk.page_content}")


    # Embedding
    embedding_model = (HuggingFaceEmbeddings(model_name ='all-MiniLM-L6-v2'))

    #Vector Database
    vectordb = (Chroma.from_documents(documents=chunks, embedding=embedding_model,
                                      collection_name = str(uuid.uuid4())))

    print(vectordb.get()['documents'])


    retriever = vectordb.as_retriever(search_kwargs = {"k" : 3})
    return retriever









