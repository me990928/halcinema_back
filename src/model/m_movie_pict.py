from sqlalchemy import Column, Integer, LargeBinary, String, DateTime, ForeignKey, Boolean
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class MoviePict(Base):
    __tablename__ = "m_movie_pict"

    movie_pict_id = Column(Integer, primary_key=True)
    movie_id = Column(String)
    movie_pict = Column(LargeBinary)
    movie_pict_encoding = Column(Boolean , default=False)

    def __repr__(self):
        return "<MoviePict('movie_id={}', movie_pict={}, movie_pict_encoding={})>".format(
            self.movie_id,
            self.movie_pict,
            self.movie_pict_encoding
        )