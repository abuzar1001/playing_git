from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    api_key=os.getenv("api_key")
)

conversation = {}

def chatbot(user_id, input_text):

    if user_id not in conversation:
        conversation[user_id] = []

    history = conversation[user_id]
   
    history.append({"role": "user", "content": input_text})

    response = client.responses.create(
        model="gpt-4o-mini",
        input=history)
    
    res = response.output_text

    history.append({"role": "assistant", "content": res})

    return res
    
