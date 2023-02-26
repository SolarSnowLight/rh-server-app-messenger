from pydantic import BaseModel

class CreateMessage(BaseModel):
    chat_id: str
    user_id: str
    message: str

class UpdateMessage(BaseModel):
    chat_id: str
    user_id: str
    message: str