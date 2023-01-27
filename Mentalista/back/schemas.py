from typing import List, Union

from pydantic import BaseModel

# ANWER
class AnwerBase(BaseModel):
  text: str
  is_correct: bool

class AnwerCreate(AnwerBase):
  pass

class Anwer(AnwerBase):
  id: int
  question_id: int
  
  class Config:
    orm_mode= True 


# QUESTION
class QuestionBase(BaseModel):
  text: str
  image: Union[str, None] = None

class QuestionCreate(QuestionBase):
  pass

class Question(QuestionBase):
  id: int
  quiz_id: int
  anwers: list[Anwer] = []
  
  class Config:
    orm_mode= True 

# QUIZ
class QuizBase(BaseModel):
  title: str
  description: Union[str, None] = None
  image: Union[str, None] = None

class QuizCreate(QuizBase):
  pass

class Quiz(QuizBase):
  id: int
  questions: List[Question] = []
  
  class Config:
    orm_mode = True