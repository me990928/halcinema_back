from sqlalchemy import Column, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class MovieTitle(Base):
    __tablename__ = 'm_movie_titles'

    f_movie_title_id = Column(String(8), primary_key=True)
    f_movie_title_japan = Column(String(50), nullable=False)
    f_movie_title_foreign = Column(String(50), nullable=False)

    def __repr__(self):
        return f"<MovieTitle(f_movie_title_id='{self.f_movie_title_id}', f_movie_title_japan='{self.f_movie_title_japan}', f_movie_title_foreign='{self.f_movie_title_foreign}')>"
