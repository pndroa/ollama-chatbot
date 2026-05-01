from fastapi import APIRouter
import requests

router = APIRouter()

@router.get("")
async def get_models():
  models_list = []
  
  response_data = requests.get("http://localhost:11434/api/tags").json()
  
  for model in response_data.get("models", []):
      model_name = model["name"]
      
      show_response = requests.post(
          "http://localhost:11434/api/show", 
          json={"name": model_name}
      ).json()
      
      capabilities = show_response.get("capabilities", [])
      has_thinking = "thinking" in capabilities
      
      models_list.append({
          "name": model_name,
          "thinking": has_thinking
      })
      
  return {"models": models_list}
    

@router.get("/{model_name}")
async def get_model(model_name: str):
    show_response = requests.post(
        "http://localhost:11434/api/show", 
        json={"name": model_name}
    ).json()

    capabilities = show_response.get("capabilities", [])
    has_thinking = "thinking" in capabilities
    
    return {"name": model_name, "thinking": has_thinking}