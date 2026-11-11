import streamlit as st
from Modules.LLMS import load_llm
from Modules.langchain_rag import build_retriver
from langchain.chains import (RetrievalQA)



st.set_page_config(
    page_title = "RAG WITH LANGCHAIN",
    page_icon = "🤖",
    layout = "wide"
)


pdf = st.file_uploader("Upload your PDF file", type="pdf")

if pdf is not None:
    with st.spinner("Processing your PDF file..."):
        retriever = build_retriver(pdf)
        llm = load_llm()
        

        qa_chain = RetrievalQA.from_chain_type(llm=llm, chain_type="stuff", retriever=retriever)
        st.success("PDF file processed successfully!")
        question = st.text_input("Ask a question about the PDF:")


        if st.button("ASK"):
            with st.spinner("Generating answer..."):
                docs = retriever.get_relevant_documents(question)
                st.subheader("retrieved documents")
                for i , doc in enumerate(docs):
                    st.write(f"Document {i+1}: {doc.page_content}")
                answer = qa_chain.run(question)
                st.write(answer)
