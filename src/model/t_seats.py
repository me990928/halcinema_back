from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Seat(Base):
    __tablename__ = 't_seats'

    f_seat_id = Column(Integer, primary_key=True)
    f_seat_number = Column(String(4), nullable=False)
    f_theater_schedule_id = Column(Integer, nullable=False)
    f_seat_status = Column(Boolean)

    def __repr__(self):
        return f"<Seat(f_seat_id={self.f_seat_id}, f_seat_number='{self.f_seat_number}', f_theater_schedule_id={self.f_theater_schedule_id}, f_seat_status={self.f_seat_status})>"
