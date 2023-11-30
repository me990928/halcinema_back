from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class GeneralInquiry(Base):
    __tablename__ = 't_general_inquiries'

    f_general_inquiry_id = Column(Integer, primary_key=True)
    f_inquiry_topic = Column(String(30), nullable=False)
    f_mail_address = Column(String(50), nullable=False)
    f_inquiry_content_path = Column(Text, nullable=False)

    def __repr__(self):
        return f"<GeneralInquiry(f_general_inquiry_id={self.f_general_inquiry_id}, f_inquiry_topic='{self.f_inquiry_topic}', f_mail_address='{self.f_mail_address}', f_inquiry_content_path='{self.f_inquiry_content_path}')>"
