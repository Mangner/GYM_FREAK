from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Float
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func 
from .database import Base



class User(Base):
    __tablename = "users"

    

