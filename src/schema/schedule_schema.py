from pydantic import BaseModel, ConfigDict
from datetime import datetime

class MovieScheduleSchema(BaseModel):
    f_movie_schedule_id: int | None = None
    f_movie_schedule_name: str
    f_movie_id: str
    f_movie_start_datetime: datetime
    f_movie_end_datetime: datetime
    model_config = ConfigDict(from_attributes=True)

class TheaterScheduleSchema(BaseModel):
    f_theater_schedule_id: int | None = None
    f_screen_id: str
    f_movie_schedule_id: int
    f_movie_start_datetime: datetime
    f_release_end_date: datetime

    model_config = ConfigDict(from_attributes=True)
