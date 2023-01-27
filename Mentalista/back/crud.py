from sqlalchemy.orm import Session

from . import models, schemas

def get_quiz(db: Session, quiz_id: int):
  return db.query(models.Quiz).filter(models.Quiz.id == quiz_id).first()

def get_quizzes(db: Session, skip: int = 0, limit: int = 0):
  return db.query(models.Quiz).offset(skip).limit(limit).all()

def create_quiz(db: Session, quiz: schemas.QuizCreate):
  db_quiz = models.Quiz(
    title= quiz.title,
    description= quiz.description,
    image= quiz.image,
  )
  
  db.add(db_quiz)
  db.commit()
  db.refresh(db_quiz)
  
  return db_quiz

def get_questions(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Question).offset(skip).limit(limit).all()

def create_questions(db: Session, question: schemas.QuestionCreate, quiz_id: int):
  db_question = models.Question(**question.dict(), quiz_id= quiz_id)
  
  db.add(db_question)
  db.commit()
  db.refresh(db_question)
  
  return db_question
  
def get_anwers(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Answer).offset(skip).limit(limit).all()

def create_questions(db: Session, anwer: schemas.AnwerCreate, question_id: int):
  db_anwer = models.Answer(**anwer.dict(), quiz_id= question_id)
  
  db.add(db_anwer)
  db.commit()
  db.refresh(db_anwer)
  
  return db_anwer