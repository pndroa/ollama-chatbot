from fastapi import APIRouter
import requests

router = APIRouter()

@router.get("")
async def get_models():
    models_list = []
    
    response_data = requests.get("http://localhost:11434/api/tags").json()
    
    for model in response_data["models"]:
        models_list.append(model["name"])
        
    return {"models": models_list}