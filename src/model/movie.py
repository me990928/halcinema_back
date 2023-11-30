from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from app.database import Base

class Movies(Base):
    __tablename__ = "movies"

    