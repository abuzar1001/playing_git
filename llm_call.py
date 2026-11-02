from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    api_key=os.getenv("api_key")
)

history = []

while True:
    user = input("User: ")
    history.append({"role": "user", "content": user})


    response = client.responses.create(
        model="gpt-4o-mini",
        messages=history)

    
    print(response.output_text)

    history.append({"role": "assistant", "content": response.output_text})
    
