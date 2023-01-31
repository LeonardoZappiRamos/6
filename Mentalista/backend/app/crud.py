from sqlalchemy.orm import Session

from . import models, schemas

# QUIZ
def create_quiz():
  """ Create a question """
  
def read_quiz(db: Session, quiz_id: int):
  """ Read a question """
  return db.query(models.Quiz).filter(models.Quiz.id == quiz_id).first()

def read_quizzes(db: Session, skip: int = 0, limit: int = 100):
  """ Read a list of quizzes """
  return db.query(models.Quiz).offset(skip).limit(limit).all()

def update_quiz():
  """ Update a question """

def delete_quiz():
  """ Delete a question """
  
# OPTION
def create_option():
  """ Create a question """
  
def read_option():
  """ Read a question """

def update_option():
  """ Update a question """

def delete_option():
  """ Delete a question """