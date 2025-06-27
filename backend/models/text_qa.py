from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

apikey = os.getenv("OPENAI_API_KEY")
client = None
if apikey:
    client = OpenAI(api_key=apikey)

def ask_openai(caption : str, question: str) -> str:
    if not client:
        return "OpenAI API key not configured. Please set OPENAI_API_KEY environment variable."
    
    system_prompt = "you are a helpful assistant who will be answering back to questions related to image captions. you will be provided image captions and you will have to be answerable to all the queries that are asked to you about them. input queries will be in the format: Image caption:  caption \nQuestion: question. you need to output the Question: question, Answer: answer"

    user_prompt = f"Image caption: {caption}\nQuestion: {question}"

    responses = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ],
        temperature=0.5,
    )

    answer = responses.choices[0].message.content.strip() if responses.choices[0].message.content else "no response"

    return answer
