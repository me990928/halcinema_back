from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class AppointmentDetail(Base):
    __tablename__ = 't_appointment_details'

    f_appointment_id = Column(Integer, primary_key=True)
    f_screen_id = Column(String(8), nullable=False)
    f_seat_number = Column(String(4), nullable=False)
    f_ticket_type_id = Column(String(8), nullable=False)
    f_appointment_detail_id = Column(Integer, nullable=False)

    def __repr__(self):
        return f"<AppointmentDetail(f_appointment_id={self.f_appointment_id}, f_screen_id='{self.f_screen_id}', f_seat_number='{self.f_seat_number}', f_ticket_type_id='{self.f_ticket_type_id}', f_appointment_detail_id={self.f_appointment_detail_id})>"
