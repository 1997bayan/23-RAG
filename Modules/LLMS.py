import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key = os.getenv("GEMINI_API_KEY"))

gemini_model = (genai.GenerativeModel("gemini-2.5-flash"))


def load_prompt():
    with open("prompts/rag_prompt.txt","r",encoding = 'utf-8') as f:
        prompt = f.read()
        return prompt


prompt_template = (load_prompt())


def ask_gemini(question, context):
    prompt = prompt_template.format(context=context ,question = question)

    response = (gemini_model.generate_context(
        prompt = prompt
    ) )


    return response.text
