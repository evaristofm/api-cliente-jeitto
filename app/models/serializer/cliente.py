from pydantic import BaseModel, Field


class ClienteRequest(BaseModel):
    username: str = Field(min_length=3)
    email: str
    phone: str


class ClienteResponse(ClienteRequest):
    id: int
