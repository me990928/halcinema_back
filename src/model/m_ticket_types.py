from sqlalchemy import Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class TicketType(Base):
    __tablename__ = 'm_ticket_types'

    f_ticket_type_id = Column(String(8), primary_key=True)
    f_ticket_type_name = Column(String(15), nullable=False)
    f_ticket_price = Column(Integer, nullable=False)

    def __repr__(self):
        return f"<TicketType(f_ticket_type_id='{self.f_ticket_type_id}', f_ticket_type_name='{self.f_ticket_type_name}', f_ticket_price={self.f_ticket_price})>"
