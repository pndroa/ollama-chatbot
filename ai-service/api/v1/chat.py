from fastapi import APIRouter
from schemas.chat import ChatRequest, ChatResponse
from logic.agent import response

router = APIRouter()

@router.post("/send")
async def send_message(ChatRequest: ChatRequest):
  # mach was
  return
  
@router.get("/get")
async def read_message():
  return {"message": response}