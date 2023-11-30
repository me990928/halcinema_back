from sqlalchemy import Column, String, Boolean, Date
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = 'm_users'

    f_user_id = Column(String(8), primary_key=True)
    f_login_name = Column(String(20), nullable=False)
    f_login_password = Column(String(20), nullable=False)
    f_news_subscribed = Column(Boolean, nullable=False)
    f_birthday = Column(Date, nullable=False)
    f_postal_code = Column(String(10), nullable=False)
    f_prefecture = Column(String(10), nullable=False)
    f_city = Column(String(20), nullable=False)
    f_address1 = Column(String(30), nullable=False)
    f_address2 = Column(String(30))
    f_mail_address = Column(String(50), nullable=False)
    f_full_name_kanji = Column(String(20), nullable=False)
    f_full_name_kana = Column(String(20), nullable=False)

    def __repr__(self):
        return f"<User(f_user_id='{self.f_user_id}', f_login_name='{self.f_login_name}', f_news_subscribed={self.f_news_subscribed}, f_birthday='{self.f_birthday}', f_postal_code='{self.f_postal_code}', f_prefecture='{self.f_prefecture}', f_city='{self.f_city}', f_address1='{self.f_address1}', f_address2='{self.f_address2}', f_mail_address='{self.f_mail_address}', f_full_name_kanji='{self.f_full_name_kanji}', f_full_name_kana='{self.f_full_name_kana}')>"
