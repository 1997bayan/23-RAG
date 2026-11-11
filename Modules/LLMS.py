import os
import google.generativeai as genai
from dotenv import load_dotenv

from langchain_google_genai import ChatGoogleGenerativeAI
load_dotenv()

#genai.configure(api_key = os.getenv("GEMINI_API_KEY"))

#gemini_model = (genai.GenerativeModel("gemini-3.8-flash"))


# def load_prompt():
#     with open("prompts/rag_prompt.txt","r",encoding = 'utf-8') as f:
#         prompt = f.read()
#         return prompt


# prompt_template = (load_prompt())


# def ask_gemini(question, context):
#     prompt = prompt_template.format(context=context ,question = question)

#     response = (gemini_model.generate_content( prompt
#     ) )


#     return response.text

def load_llm():
    llm = ChatGoogleGenerativeAI(model="gemini-3.8-flash",api_key=os.getenv("GEMINI_API_KEY"),
                                 temperature=0.2,max_output_tokens=512)
    return llm