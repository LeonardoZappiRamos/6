from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .database import Base

class Option(Base):
  __tablename__ = "options"
  
  id: Column(Integer, primary_key=True, index=True)
  descrition: Column(String)
  quiz_id: Column(Integer)
  
  quiz = relationship('Quiz', back_populates= "options")
  
class Quiz(Base):
  __tablename__ = "quizzes"
  
  id: Column(Integer, primary_key=True, index=True)
  title: Column(String)
  answer: Column(Integer)
  
  options = relationship('Option', back_populates= "quiz")