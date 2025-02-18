from typing import Literal
from pydantic import BaseModel

class Ability(BaseModel):
    name: str
    description: str
    is_hidden: bool