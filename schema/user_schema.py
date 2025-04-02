from pydantic import BaseModel

class registerUser(BaseModel):
    name: str
    phone: str
    id: str
    password: str