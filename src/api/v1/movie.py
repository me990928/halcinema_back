from fastapi import APIRouter
from fastapi.params import Depends

import sys

from sqlalchemy import select
sys.path.append("../../")

from app.database import get_db
from model.m_movies import Movie
from model.m_movie_titles import MovieTitle
from schema.movie_schema import MovieSchema
from sqlalchemy.orm import Session
from crud.movie import add_movie_title
from schema.movie_schema import MovieTitleSchema
from itertools import chain
router = APIRouter()

@router.get("/", tags=["movie"])
def read_root():
    return {"root": "Movie API"}

@router.get("/get")
def get_movie1(db: Session = Depends(get_db)):
    q = db.query(Movie, MovieTitle).join(Movie, Movie.f_movie_title_id == MovieTitle.f_movie_title_id).limit(100).all()  
    return [{k: v for k, v in chain(movie.__dict__.items(), title.__dict__.items()) if not k.startswith('_')} for movie, title in q]
 
@router.post("/create")
def add_movie(movie_schema: MovieSchema, db: Session = Depends(get_db)):
    # f_movie_idを取得するクエリを作成
    query = select(Movie.f_movie_id).order_by(Movie.f_movie_id.desc()).limit(1)
    result = db.execute(query)

    # クエリ結果からf_movie_idを取得
    f_movie_id = result.scalar()

    try:
        new_f_movie_id = increment_f_movie_id(f_movie_id)
    except:
        new_f_movie_id = "MG000001"

    movie_schema.f_movie_id = new_f_movie_id

    movie = Movie(**movie_schema.dict())
    db.add(movie)
    db.commit()
    db.refresh(movie)
    return {"msg": "success", "f_movie_id": new_f_movie_id}

def increment_f_movie_id(f_movie_id):
    # f_movie_idの現在の値を取得
    current_value = int(f_movie_id[2:])

    # f_movie_idをインクリメント
    incremented_value = current_value + 1

    # インクリメントされたf_movie_idをMG000001のような形式に変換
    new_f_movie_id = "MG" + str(incremented_value).zfill(6)

    return new_f_movie_id

@router.post("/create_title")
def create_movie_title(movie_title_schema: MovieTitleSchema, db: Session = Depends(get_db)):
    return add_movie_title(movie_title_schema, db)