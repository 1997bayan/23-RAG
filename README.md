# RAG PDF Chatbot

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.9%2B-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python 3.9+" />
  <img src="https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white" alt="Streamlit" />
  <img src="https://img.shields.io/badge/Gemini-AI-8A2BE2?style=for-the-badge" alt="Gemini AI" />
  <img src="https://img.shields.io/badge/RAG-Document%20QA-0A0A0A?style=for-the-badge" alt="RAG Document QA" />
</p>

A lightweight Retrieval-Augmented Generation (RAG) application that lets users upload a PDF and ask questions about its content in natural language. The app extracts text, splits it into chunks, embeds the chunks, retrieves the most relevant context, and sends it to a Gemini model for a grounded answer.

## Overview

This project demonstrates a practical document Q&A workflow using modern AI and vector search:

- PDF text extraction
- Chunk-based document segmentation
- Embedding generation with Sentence Transformers
- Semantic retrieval from a vector database
- Context-aware answer generation with Google Gemini
- Interactive UI powered by Streamlit

## Features

- Upload a PDF file directly in the browser
- Extract text from PDF pages using `pypdf`
- Split long documents into manageable chunks
- Generate embeddings using `all-MiniLM-L6-v2`
- Store embeddings in Chroma for similarity search
- Retrieve the top relevant passages for a user query
- Generate answers grounded in the retrieved content
- Provide a clean, user-friendly Streamlit interface

## Architecture

The application follows a standard RAG pipeline:

1. The user uploads a PDF.
2. The PDF is converted into raw text.
3. The text is split into chunks.
4. Each chunk is embedded and stored in a vector database.
5. A question is encoded and compared against the stored vectors.
6. The most relevant chunks are retrieved.
7. The retrieved context is appended to the prompt.
8. Gemini generates a response based on that context.

## Project Structure

```text
23-RAG/
├── app.py
├── README.md
├── requirements.txt
├── Note.ipynb
├── test rag.pages
├── test rag.pdf
├── Modules/
│   ├── LLMS.py
│   ├── __init__.py
│   ├── embedding.py
│   ├── pdf_utlis.py
│   └── vector_database.py
├── prompts/
│   └── rag_prompt.txt
├── .env
└── .venv/
```

## Tech Stack

- Python
- Streamlit
- PyPDF
- Sentence Transformers
- Chroma
- Google Generative AI (Gemini)
- Python-dotenv

## Prerequisites

Before running this project, make sure you have:

- Python 3.9 or newer
- A valid Google Gemini API key
- A virtual environment for dependency isolation

## Installation

1. Clone the repository:

```bash
git clone https://github.com/1997bayan/23-RAG.git
cd 23-RAG
```

2. Create a virtual environment:

```bash
python -m venv .venv
source .venv/bin/activate   # macOS/Linux
# or
.venv\Scripts\activate      # Windows
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

## Configuration

Create a `.env` file in the project root and add your Gemini API key:

```env
GEMINI_API_KEY=your_api_key_here
```

## Run the App

Start the application with:

```bash
streamlit run app.py
```

Then open the local URL displayed in the terminal (usually `http://localhost:8501`).

## Usage

1. Upload a PDF file.
2. Wait for the document to be processed.
3. Enter a question about the document.
4. Click the action button to generate an answer.
5. Review both the retrieved context and the final answer.

## Example Workflow

```text
User Question: "What are the main ideas discussed in this document?"

1. Query is embedded
2. Top matching chunks are retrieved
3. Relevant context is sent to Gemini
4. Gemini responds with an answer grounded in the PDF content
```

## How RAG Works Here

This project uses a classic retrieval-based pipeline:

- The PDF is converted into text.
- Text is split into short chunks.
- Each chunk is embedded into a vector representation.
- The user question is also embedded.
- Semantically similar chunks are selected from the vector database.
- The selected chunks are inserted into the prompt for the language model.
- The LLM answers using the relevant document context instead of relying solely on its pre-trained knowledge.

## Project Notes

- Retrieval quality depends on document quality and chunk size.
- Better results usually come from well-structured chunks and meaningful segmentation.
- This app is suitable as a learning project or a foundation for a production-ready document assistant.

## Future Improvements

- Add chunk overlap for better retrieval continuity
- Support multi-document collections
- Add persistent vector storage
- Improve result ranking and response grounding
- Add conversation history for multi-turn Q&A
- Add document metadata and filtering options

## License

This project currently does not include a license file. If you plan to distribute or reuse it publicly, consider adding an appropriate open-source license.

## Contributing

Contributions are welcome. If you want to improve the project, you can:

- improve document chunking and retrieval logic
- enhance the prompt strategy
- optimize the Streamlit interface
- add better error handling and validation

## Contact

For questions or collaboration opportunities, connect with the project owner through the repository or profile linked on GitHub.


