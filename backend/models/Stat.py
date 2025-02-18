from typing import Literal
from pydantic import BaseModel

class Stat(BaseModel):
    name: str
    value: int