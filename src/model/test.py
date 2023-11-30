from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from app.database import Base

class Test(Base):
    __tablename__ = "test"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    fullname = Column(String)
    nickname = Column(String)

    def __repr__(self):
        return "<User('name={}', fullname={}, nickname={})>".format(
            self.name,
            self.fullname,
            self.nickname
        )
