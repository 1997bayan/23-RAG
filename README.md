# RAG project (Retrieval-Augmented Generation)


## How to Get in:





## Thoughts:------

### Clone repo:
``` git clone [repo-name] ```

### creaye .env file:
``` cp .env.example.env```
  -GEMINI_API_KEY = your_api_key_here

ChatGpt : chat bot [predections] --> RNN ,LSTM,Transformer[Attention],[GPT Decoder]

GPT pre-train NN 'NOT LIVE'
+ Bring LLM to live:
  - Fine Tuning: Re-train -> Model [time] + [money] + [data]
  - RAG -> (Retrieval-Augmented Generation)
        - Retrieve: Find information relevant to the user’s question.
        -  Augment: Add that information to the AI’s prompt as context.


## Project Goal:
 - user [pdf] ---> chat with pdf (Q&A)
 - PDF --> emedding [Vectors]
 - Vectors --> add to vector (dataBase)
 - user query (ask question ): ---> embedding ---> similarity [Best match]
 - so i have [[query contenxt]] <-- similarity --> [[vector database context]]
 - prompt + {user_context} ----> LLMS --> answer 


 ## Structure :
 - app.py
 - Modules :
    - __init__.py
    - pdf_utlis.py
    - embedding.py
    - vector_database.py
    - LLMS.py
 - prompts/
    rag_prompt.txt
 - .env
 - req.txt



