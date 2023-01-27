from typing import List

from fastapi import FastAPI, Depends

from sqlalchemy.orm import Session

from . import crud, models, schemas
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind= engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/api/quiz/", response_model= List[schemas.Quiz])
async def read_quizzes(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
  '''Read a list of quizzes from the database'''
  
  quizzes = crud.get_quizzes(db, skip=skip, limit=limit)
  return quizzes

@app.get("/api/quiz/", response_model= schemas.Quiz)
async def read(id: int = None):
  '''Read a list of quizzes or one quiz from the database'''
  
  if id is None:
    return {"message": "A list of quiz"}
  else:
    return {"message": "A quiz id {}".format(id)}

@app.post("/api/quiz/")
async def create(quiz: Quizzes):
  '''Create a new quiz'''
  
  return {"message": "Quiz Created"}
  
@app.post("/api/quiz/{id_quiz}/question/")
async def create(question: Questions):
  '''Create a new Question to a quiz'''
  
  return {"message": "Question Created"}
  
@app.post("/api/quiz/{id_quiz}/question/{id_question}/answers")
async def create(answer: Answers):
  '''Create a new answer to a question'''
  
  return {"message": "Answers Created"}