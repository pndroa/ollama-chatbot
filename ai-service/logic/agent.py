from langchain.messages import HumanMessage
from langchain_core.messages import ChatMessage
from core.config import llm_model

messages = [
  ChatMessage(role="control", content="thinking"),
  HumanMessage("Write me a little story")
]

response = llm_model.invoke(messages)