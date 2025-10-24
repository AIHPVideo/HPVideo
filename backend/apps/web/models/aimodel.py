from pydantic import BaseModel
from typing import Optional

class AiModelReq(BaseModel):
    project: str
    source: str
    model: str
    duration: int
    messages: object
    image: Optional[str] = None
    size: str

class AiResultReq(BaseModel):
    requestId: str
