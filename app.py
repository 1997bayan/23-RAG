import streamlit as st

from Modules.LLMS import ask_gemini
from Modules.vector_database import build_vector_database, retrieve_context
from Modules.pdf_utlis import extract_text_from_pdf, chunk_text

st.set_page_config(
    page_title="RAG PDF Chatbot",
    page_icon="📄",
    layout="wide",
)

st.markdown(
    """
    <style>
        :root {
            --bg: #0b1020;
            --panel: rgba(17, 24, 39, 0.9);
            --panel-strong: #111827;
            --primary: #7c3aed;
            --primary-soft: #a78bfa;
            --text: #e5e7eb;
            --muted: #a1a1aa;
            --success: #34d399;
            --border: rgba(148, 163, 184, 0.2);
        }

        html, body, [data-testid="stAppViewContainer"] {
            background: linear-gradient(135deg, #0b1020 0%, #111827 50%, #1f2937 100%);
            color: var(--text);
        }

        [data-testid="stSidebar"] {
            background: rgba(15, 23, 42, 0.95);
            border-right: 1px solid var(--border);
        }

        .hero {
            background: linear-gradient(135deg, rgba(124, 58, 237, 0.18), rgba(59, 130, 246, 0.08));
            border: 1px solid var(--border);
            border-radius: 20px;
            padding: 2rem 1.5rem;
            margin-bottom: 1.5rem;
            box-shadow: 0 18px 40px rgba(15, 23, 42, 0.25);
        }

        .hero h1 {
            margin: 0;
            font-size: 2.4rem;
            font-weight: 700;
            letter-spacing: -0.04em;
        }

        .hero p {
            margin-top: 0.5rem;
            color: var(--muted);
            font-size: 1rem;
        }

        .metric-card {
            background: rgba(17, 24, 39, 0.8);
            border: 1px solid var(--border);
            border-radius: 16px;
            padding: 1rem;
            box-shadow: 0 12px 24px rgba(15, 23, 42, 0.18);
        }

        .answer-box {
            background: rgba(15, 23, 42, 0.9);
            border: 1px solid rgba(167, 139, 250, 0.35);
            border-radius: 18px;
            padding: 1.25rem 1.25rem;
            margin-top: 0.8rem;
            color: var(--text);
            line-height: 1.7;
        }

        .stFileUploader > div {
            background: rgba(17, 24, 39, 0.7);
            border: 1px dashed rgba(167, 139, 250, 0.4);
            border-radius: 18px;
        }

        .stTextArea textarea, .stTextInput input {
            background: rgba(15, 23, 42, 0.8);
            color: var(--text);
            border: 1px solid var(--border);
            border-radius: 14px;
        }

        .stButton > button {
            background: linear-gradient(135deg, var(--primary), #2563eb);
            color: white;
            border: none;
            border-radius: 12px;
            font-weight: 600;
            padding: 0.7rem 1.4rem;
            box-shadow: 0 12px 24px rgba(124, 58, 237, 0.35);
        }

        .stButton > button:hover {
            filter: brightness(1.08);
        }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
    <div class="hero">
        <h1>📄 RAG PDF Chatbot</h1>
        <p>Upload a document, ask a question, and get a grounded answer from the most relevant content in your PDF.</p>
    </div>
    """,
    unsafe_allow_html=True,
)

with st.sidebar:
    st.markdown("### About")
    st.write(
        "This assistant uses Retrieval-Augmented Generation to find the most relevant parts of a PDF and answer your questions with context-aware reasoning."
    )
    st.markdown("---")
    st.markdown("### Workflow")
    st.write("1. Upload a PDF\n2. Extract and chunk text\n3. Generate embeddings\n4. Retrieve relevant passages\n5. Ask Gemini for the answer")

uploaded_file = st.file_uploader("Upload a PDF document", type=["pdf"], help="Supported format: PDF")

if uploaded_file is not None:
    with st.spinner("Processing your PDF..."):
        text = extract_text_from_pdf(uploaded_file)
        chunks = chunk_text(text)
        collection = build_vector_database(chunks)

    st.success(f"Successfully processed the document with {len(chunks)} text chunks.")

    col1, col2, col3 = st.columns(3)
    col1.markdown(
        """
        <div class="metric-card">
            <div style="color: #a1a1aa; font-size: 0.8rem;">Filename</div>
            <div style="font-size: 1.1rem; font-weight: 600; margin-top: 0.35rem;">{}</div>
        </div>
        """.format(uploaded_file.name),
        unsafe_allow_html=True,
    )
    col2.markdown(
        """
        <div class="metric-card">
            <div style="color: #a1a1aa; font-size: 0.8rem;">Text Chunks</div>
            <div style="font-size: 1.1rem; font-weight: 600; margin-top: 0.35rem;">{}</div>
        </div>
        """.format(len(chunks)),
        unsafe_allow_html=True,
    )
    col3.markdown(
        """
        <div class="metric-card">
            <div style="color: #a1a1aa; font-size: 0.8rem;">Status</div>
            <div style="font-size: 1.1rem; font-weight: 600; margin-top: 0.35rem; color: #34d399;">Ready</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown("### Ask a question")
    question = st.text_area(
        "",
        placeholder="Example: What are the key findings in this document?",
        height=120,
    )

    if st.button("Generate Answer", use_container_width=True):
        if not question.strip():
            st.warning("Please enter a question before generating an answer.")
        else:
            with st.spinner("Finding the best matches in your document..."):
                context = retrieve_context(question, collection)

            with st.spinner("Generating a response from the retrieved context..."):
                answer = ask_gemini(question, context)

            st.markdown("### Retrieved Context")
            st.code(context[:4000], language="text")

            st.markdown("### Final Answer")
            st.markdown(f"<div class='answer-box'>{answer}</div>", unsafe_allow_html=True)
else:
    st.info("Upload a PDF to begin your document Q&A session.")

