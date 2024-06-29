from pydantic import BaseModel

class BaseSchema(BaseModel):
    status: str
    message: str | None = None


class ResponseSchema(BaseSchema):
    data: list
