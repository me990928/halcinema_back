import sys
sys.path.append("../../")

from fastapi import APIRouter
from fastapi import Depends
from sqlalchemy.orm import Session
from app.database import get_db
from model.t_theater_schedules import TheaterSchedule, MovieSchedule
from schema.schedule_schema import MovieScheduleSchema


router = APIRouter()

@router.get("/", tags=["schedule"])
def read_root():
    return {"root": "schedule API"}

@router.post("/movie")
def add_movie_schedule(movie_schedule_schema: MovieScheduleSchema, db: Session = Depends(get_db)):
    movie_schedule = MovieSchedule(**movie_schedule_schema.dict())
    db.add(movie_schedule)
    db.commit()
    return {"msg": "success"}