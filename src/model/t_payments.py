from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Payment(Base):
    __tablename__ = 't_payments'

    f_payment_id = Column(Integer, primary_key=True)
    f_mail_address = Column(String(30), nullable=False)
    f_phone_number = Column(String(15), nullable=False)
    f_expiration_date = Column(Integer, nullable=False, comment='YYYYMM')
    f_card_holder_name = Column(String(40), nullable=False)

    def __repr__(self):
        return f"<Payment(f_payment_id={self.f_payment_id}, f_mail_address='{self.f_mail_address}', f_phone_number='{self.f_phone_number}', f_expiration_date={self.f_expiration_date}, f_card_holder_name='{self.f_card_holder_name}')>"
