from fastapi import FastAPI
from pydantic import BaseModel
from src.llm_call import chatbot

app = FastAPI()

class ChatbotRequest(BaseModel):
    message: str
    user_id: str

class ChatbotResponse(BaseModel):
    response: str

@app.post("/chatbot", response_model=ChatbotResponse)
def chat(request: ChatbotRequest):
    response_text = chatbot(request.message, request.user_id)
    return ChatbotResponse(response=response_text)