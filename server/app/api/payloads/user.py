from pydantic import BaseModel


class UserPayload(BaseModel):
    username: str
