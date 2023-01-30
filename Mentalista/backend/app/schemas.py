from typing import List, Union

from pydantic import BaseModel

class Quiz(BaseModel):
  title: str
  options: List[str]
  answer: int