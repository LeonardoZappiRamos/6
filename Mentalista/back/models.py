from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .database import Base

class Quiz(Base):
  '''The representetion of a Quiz'''
  __tablename__ = 'quizzes'
  
  id: Column(Integer, primary_key= True, index= True)
  title: Column(String)
  description: Column(String)
  image: Column(String)
  
  questions = relationship("Question", back_populated= "quiz")

class Question(Base):
  '''The representetion of a Question'''
  __tablename__ = 'questions'
  
  id: Column(Integer, primary_key= True, index= True)
  text: Column(String)
  image: Column(String)
  quiz_id: Column(Integer, ForeignKey('quizzes.id'))
  
  quiz = relationship("Quiz", back_populates= "questions")
  anwers = relationship("Answer", back_populates= "questions")

class Answer(Base):
  '''The representetion of a Answer'''
  __tablename__ = 'anwers'
  
  id: Column(Integer, primary_key=True, index=True)
  text: Column(String)
  is_correct: Column(Boolean)
  question_id: Column(Integer, ForeignKey("questions.id"))
  
  question = relationship("Question", back_populates= "anwers")