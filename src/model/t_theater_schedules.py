from sqlalchemy import Column, Integer, String, DateTime, Date
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class TheaterSchedule(Base):
    __tablename__ = 't_theater_schedules'

    f_theater_schedule_id = Column(Integer, primary_key=True)
    f_screen_id = Column(String(8), nullable=False)
    f_movie_id = Column(String(8), nullable=False)
    f_movie_start_datetime = Column(DateTime, comment='上映開始時間')

    f_release_end_date = Column(Date)

    def __repr__(self):
        return f"<TheaterSchedule(f_theater_schedule_id={self.f_theater_schedule_id}, f_screen_id='{self.f_screen_id}', f_movie_id='{self.f_movie_id}', f_movie_start_datetime='{self.f_movie_start_datetime}', f_movie_end_datetime='{self.f_movie_end_datetime}', f_release_date='{self.f_release_date}', f_release_end_date='{self.f_release_end_date}')>"

class MovieSchedule(Base):
    __tablename__ = 't_movie_schedules'

    f_movie_schedule_id = Column(Integer, primary_key=True)
    f_movie_schedule_name = Column(String(255), nullable=False)
    f_movie_id = Column(String(8), nullable=False)
    f_movie_start_datetime = Column(DateTime, comment='上映開始日')
    f_movie_end_datetime = Column(DateTime, comment='上映終了日')

    def __repr__(self):
        return f"<MovieSchedule(f_movie_schedule_id={self.f_movie_schedule_id}, f_movie_schedule_name='{self.f_movie_schedule_name}', f_movie_id='{self.f_movie_id}', f_movie_start_datetime='{self.f_movie_start_datetime}', f_movie_end_datetime='{self.f_movie_end_datetime}')>"