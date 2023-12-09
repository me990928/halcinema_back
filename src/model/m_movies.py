from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import event
from sqlalchemy import func

Base = declarative_base()

class Movie(Base):
    __tablename__ = 'm_movies'

    f_movie_id = Column(String(8), primary_key=True)
    f_movie_title_id = Column(String(8), nullable=False)
    f_genre_id = Column(String(8), nullable=False)
    f_content = Column(Text, nullable=False)
    f_movie_runtime_min = Column(Integer, nullable=False)
    f_movie_data = Column(Text, nullable=False)

    def __repr__(self):
        return f"<Movie(f_movie_id='{self.f_movie_id}', f_movie_title_id='{self.f_movie_title_id}', f_genre_id='{self.f_genre_id}', f_content='{self.f_content}', f_movie_runtime_min={self.f_movie_runtime_min}, f_movie_data='{self.f_movie_data}')>"
