import sys
sys.path.append("../../")

from fastapi import APIRouter
from fastapi import Depends
from sqlalchemy.orm import Session
from app.database import get_db
from model.t_theater_schedules import TheaterSchedule, MovieSchedule
from model.m_movies import Movie
from schema.schedule_schema import MovieScheduleSchema
from sqlalchemy import select
from itertools import chain




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

@router.get("/movieshcedule")
def get_movie_schedule(db: Session = Depends(get_db)):
    q = db.query(MovieSchedule.f_movie_schedule_id, MovieSchedule.f_movie_schedule_name, Movie.f_movie_runtime_min).join(Movie, Movie.f_movie_id == MovieSchedule.f_movie_id).limit(100)
    return [{"movie_schedule_id": movie_schedule_id, "movie_schedule_name": movie_schedule_name, "movie_runtime_min": movie_runtime_min} for movie_schedule_id, movie_schedule_name, movie_runtime_min in q]