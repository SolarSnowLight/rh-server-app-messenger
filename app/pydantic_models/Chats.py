from pydantic import BaseModel

class CreateChat(BaseModel):
    user_id1: str
    user_id2: str

class UpdateChat(BaseModel):
    user_id1: str
    user_id2: str