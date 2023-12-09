from sqlalchemy import Column, Integer, LargeBinary, String, DateTime, ForeignKey, Boolean
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class MoviePict(Base):
    __tablename__ = "m_movie_pict"

    f_movie_pict_id = Column(Integer ,primary_key=True, autoincrement=True)
    f_movie_id = Column(String)
    f_movie_pict = Column(String)

    def __init__(self, f_movie_id, f_movie_pict):
        self.f_movie_id = f_movie_id
        self.f_movie_pict = f_movie_pict