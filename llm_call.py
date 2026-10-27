from openai import OpenAI

client = OpenAI(
    api_key="Enter your key"
)

response = client.responses.create(
    model="gpt-4o-mini",
    input= "input text")

print(response.output_text)
    
