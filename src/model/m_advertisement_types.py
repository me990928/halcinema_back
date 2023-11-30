from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class AdvertisementType(Base):
    __tablename__ = 'm_advertisement_types'

    f_advertisement_type_id = Column(String(8), primary_key=True)
    f_advertisement_type_name = Column(String(10), nullable=False)

    def __repr__(self):
        return f"<AdvertisementType(f_advertisement_type_id='{self.f_advertisement_type_id}', f_advertisement_type_name='{self.f_advertisement_type_name}')>"
