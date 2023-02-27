from pydantic import BaseModel

class CreateChat(BaseModel):
    user_id1: int
    user_id2: int

class UpdateChat(BaseModel):
    user_id1: int
    user_id2: int