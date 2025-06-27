from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

apikey = os.getenv("OPENAI_API_KEY")
client = None

if apikey:
    try:
        client = OpenAI(api_key=apikey)
        client.models.list()
        print("OpenAI client initialized successfully")
    except Exception as e:
        print(f"Error initializing OpenAI client: {str(e)}")
        client = None

def ask_openai(caption: str, question: str) -> str:
    """Ask OpenAI a question about the image caption"""
    if not client:
        return "OpenAI API key not configured. Please set OPENAI_API_KEY environment variable."
    
    if not caption or not question:
        return "Error: Both caption and question are required."
    
    system_prompt = """You are a helpful assistant who provides detailed and comprehensive answers about image captions. 
    You will be provided with image captions and questions about them. 
    
    Please provide thorough, detailed answers that:
    - Explain your reasoning clearly
    - Include relevant details from the caption
    - Provide context and insights when possible
    - Be informative and educational
    - Use 2-4 sentences minimum for most answers
    
    If the caption doesn't contain enough information to answer the question, explain what information is missing and what you can infer from what's available.
    Keep your answers informative and engaging while being accurate to the caption content."""
    
    user_prompt = f"Image caption: {caption}\nQuestion: {question}"

    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt}
            ],
            temperature=0.7, 
            max_tokens=500,  
        )

        answer = response.choices[0].message.content.strip() if response.choices[0].message.content else "No response generated"
        return answer
        
    except Exception as e:
        error_msg = f"Error getting response from OpenAI: {str(e)}"
        print(error_msg)
        return error_msg
