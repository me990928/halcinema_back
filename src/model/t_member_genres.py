from sqlalchemy import Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class MemberGenre(Base):
    __tablename__ = 't_member_genres'

    f_user_id = Column(String(8), primary_key=True)
    f_genre_id = Column(String(8), primary_key=True)
    f_member_genre_id = Column(Integer, nullable=False)

    def __repr__(self):
        return f"<MemberGenre(f_user_id='{self.f_user_id}', f_genre_id='{self.f_genre_id}', f_member_genre_id={self.f_member_genre_id})>"
