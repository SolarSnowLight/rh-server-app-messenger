from pydantic import BaseModel

class CreateUser(BaseModel):
    name: str
    avatar: str

class UpdateUser(BaseModel):
    name: str
    avatar: str