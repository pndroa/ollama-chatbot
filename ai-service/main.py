from fastapi import FastAPI
from api.v1.chat import router as chat_router
from api.v1.models import router as model_router
from logic.agent import response

app = FastAPI()

app.include_router(chat_router, prefix="/api/v1/chat", tags=["Chat"])
app.include_router(model_router, prefix="/api/v1/models", tags=["Models"])

@app.get("/")
async def root():
    return {"status": "Service is running"}