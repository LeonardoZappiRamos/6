from typing import List, Union
from pydantic import BaseModel

class BaseOption(BaseModel):
  descrition: str

class CreateOption(BaseOption):
  pass

class Option(BaseOption):
    id: int
    quiz_id: int
    
    class Config:
        orm_mode = True

class BaseQuiz(BaseModel):
  title: str

class CreateQuiz(BaseQuiz):
  pass

class Quiz(BaseQuiz):
  id: int
  options = List[Option] = []
  answer: int
  
  class Config:
        orm_mode = True