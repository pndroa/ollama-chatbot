from fastapi import FastAPI
from api.v1.models import router as model_router

app = FastAPI()

app.include_router(model_router, prefix="/api/v1/models", tags=["Models"])

@app.get("/")
async def root():
    return {"status": "Service is running"}