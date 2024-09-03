from pydantic import BaseModel

class Chat_Bot_Model(BaseModel):
    question: str
