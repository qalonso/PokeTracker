from typing import Literal
from enum import Enum
from pydantic import BaseModel

class Category(str, Enum):
    physical = "physical"
    special = "special"
    status = "status"

class Move(BaseModel):
    name: str
    power: int
    accuracy: int
    pp: int
    type: str
    category: Category