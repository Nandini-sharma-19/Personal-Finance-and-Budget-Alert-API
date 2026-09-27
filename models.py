from sqlalchemy import Column, Integer, String,Float,DateTime,ForeignKey
from sqlalchemy.orm import relationship,declarative_base
import datetime

Base=declarative_base()

class User(Base):
  __tablename__="users"
  id=Column(Integer,primary_key=True,index=True)
  username=Column(String,unique=True,nullable=False)
  monthly_limit=Column(Float,default=10000.0)
  # Establishes relationship link to the Expense table
  expenses=relationship("Expense",back_populates="owner")

class Expense(Base):
  __tablename__="expenses"

  id=Column(Integer,primary_key=True,index=True)
  amount=Column(Float,nullable=False)
  category=Column(String,nullable=False)
  timestamp=Column(DateTime,default=datetime.datetime.utcnow)
  # Foreign key linking this specific expense to a User ID
  user_id=Column(Integer,ForeignKey("users.id"),nullable=False)
  # Links back to the user object
  owner=relationship("User",back_populates="expenses")
