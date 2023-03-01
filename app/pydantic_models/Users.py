from pydantic import BaseModel

class CreateUser(BaseModel):
    name: str

class UpdateUser(BaseModel):
    name: str