from sqlalchemy import Column, Integer, DateTime, String
from sqlalchemy.ext.declarative import declarative_base
import datetime

Base = declarative_base()

class Appointment(Base):
    __tablename__ = 't_appointments'

    f_appointment_id = Column(Integer, primary_key=True)
    f_theater_schedule_id = Column(Integer, nullable=False)
    f_completed_datetime = Column(DateTime, nullable=False, default=datetime.datetime.utcnow)
    f_payment_id = Column(Integer, nullable=False)
    f_user_id = Column(String(8), nullable=False)

    def __repr__(self):
        return f"<Appointment(f_appointment_id={self.f_appointment_id}, f_theater_schedule_id={self.f_theater_schedule_id}, f_completed_datetime='{self.f_completed_datetime}', f_payment_id={self.f_payment_id}, f_user_id='{self.f_user_id}')>"
