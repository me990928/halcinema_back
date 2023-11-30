from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Advertisement(Base):
    __tablename__ = 'm_advertisements'

    f_advertisement_id = Column(String(8), primary_key=True)
    f_advertisement_path = Column(String(100), nullable=False)
    f_priority = Column(Integer, nullable=False, default=0)
    f_advertisement_type_id = Column(String(8), nullable=False)
    f_movie_id = Column(String(8), nullable=False)

    def __repr__(self):
        return f"<Advertisement(f_advertisement_id='{self.f_advertisement_id}', f_advertisement_path='{self.f_advertisement_path}', f_priority={self.f_priority}, f_advertisement_type_id='{self.f_advertisement_type_id}', f_movie_id='{self.f_movie_id}')>"
