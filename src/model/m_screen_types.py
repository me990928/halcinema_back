from sqlalchemy import Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class ScreenType(Base):
    __tablename__ = 'm_screen_types'

    f_screen_type_id = Column(String(8), primary_key=True)
    f_columns = Column(Integer, nullable=False)
    f_rows = Column(Integer, nullable=False)

    def __repr__(self):
        return f"<ScreenType(f_screen_type_id='{self.f_screen_type_id}', f_columns={self.f_columns}, f_rows={self.f_rows})>"
