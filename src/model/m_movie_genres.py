from sqlalchemy import Column, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class MovieGenre(Base):
    __tablename__ = 'm_movie_genres'

    f_genre_id = Column(String(8), primary_key=True)
    f_genre_name = Column(String(15), nullable=False)

    def __repr__(self):
        return f"<MovieGenre(f_genre_id='{self.f_genre_id}', f_genre_name='{self.f_genre_name}')>"
