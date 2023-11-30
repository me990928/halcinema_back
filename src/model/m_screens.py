from sqlalchemy import Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Screen(Base):
    __tablename__ = 'm_screens'

    f_screen_id = Column(String(8), primary_key=True)
    f_screen_number = Column(Integer, nullable=False)
    f_screen_type_id = Column(String(8), nullable=False)

    def __repr__(self):
        return f"<Screen(f_screen_id='{self.f_screen_id}', f_screen_number={self.f_screen_number}, f_screen_type_id='{self.f_screen_type_id}')>"
