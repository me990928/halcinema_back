import os
from fastapi import APIRouter, File, UploadFile, Form
from fastapi.params import Depends
from typing import List, Optional, Any
import sys
from PIL import Image
import logging
import base64
import io

from sqlalchemy import select
sys.path.append("../../")

from app.database import get_db
from model.m_movies import Movie
from model.m_movie_titles import MovieTitle
from schema.movie_schema import MovieSchema
from sqlalchemy.orm import Session
from crud.movie import add_movie_title
from schema.movie_schema import MovieTitleSchema
from schema.movie_schema import MoviePictSchema
from itertools import chain
from model.m_movie_pict import MoviePict
from fastapi import FastAPI, Request, status
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from model.m_movie_genres import MovieGenre
from schema.movie_schema import MovieGenreSchema

router = APIRouter()

@router.get("/", tags=["movie"])
def read_root():
    return {"root": "Movie API"}

@router.get("/get")
def get_movie1(db: Session = Depends(get_db)):
    # q = db.query(Movie, MovieTitle).join(Movie, Movie.f_movie_title_id == MovieTitle.f_movie_title_id).limit(100).all()  
    # クエリを作成
    q = db.query(
        Movie,
        MovieTitle,
        MovieGenre
    ).join(
        MovieGenre, Movie.f_genre_id == MovieGenre.f_genre_id
    ).join(
        MovieTitle, Movie.f_movie_title_id == MovieTitle.f_movie_title_id
    ).limit(100)
    return [{k: v for k, v in chain(movie.__dict__.items(), title.__dict__.items(), genre.__dict__.items()) if not k.startswith('_')} for movie, title, genre in q]
 
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

# @router.post("/upload_picture")
# async def upload_picture(f_movie_pict_id: Optional[int] = Form(None), f_movie_id: str = Form(...), f_movie_pict: str = Form(...), files: List[UploadFile] = File(...), db: Session = Depends(get_db)):

   
#     # filesの要素数をログ出力
#     logging.info(f"Number of files: {len(files)}")


#     try:
#         for file in files:
#             if file.content_type != "image/jpeg":
#                 return {"msg": "画像の拡張子はjpegにしてください"}
#     except:
#         return {"msg": "画像の拡張子はjpegにしてください"}

#     try:
#         for file in files:
#             file_path = f"../../images/{f_movie_id}/{f_movie_pict}.jpeg"
#             os.makedirs(os.path.dirname(file_path), exist_ok=True)
#             with open(file_path, "wb") as buffer:
#                 buffer.write(file.file.read())
#     except:
#         return {"msg": "画像の保存に失敗しました"}

#     movie_pict_schema = MoviePictSchema(f_movie_id=f_movie_id, f_movie_pict=f_movie_pict)
#     movie_pict = MoviePict(**movie_pict_schema.dict(exclude={"f_movie_pict_id"}))
#     db.add(movie_pict)
#     db.commit()
#     db.refresh(movie_pict)

#     return {"msg": "success"}

@router.post("/upload_picture")
async def upload_files(movieId: str = Form(...), image: UploadFile = File(...), name: str = Form(...)):
    # movieIdとfile_data（UploadFile）がリクエストで受け取られる
    # contents = await file_data.read()
    # contentsにはファイルのバイナリデータが含まれます

    # ここでcontentsを処理する（例：保存する、変換する、または画像として扱うなど）

    print(name)

    # 画像をバイナリデータに変換
    contents = await image.read()

    # print(contents.decode("utf-8"))

    # print(type(contents))

    # bytesをstrに変換
    contents_str = contents.decode("utf-8")
    base64_str = contents_str.split(",")[1]

    # print(base64_str)

    # フォルダが無kレバーない場合は作成
    os.makedirs(f"../../images/{movieId}", exist_ok=True)

    # strを画像に変換
    img = Image.open(io.BytesIO(base64.b64decode(base64_str)))
    img.save(f"../../images/{movieId}/{name}.jpeg", "JPEG")
    
    return {"movieId": movieId}

@router.get("/genre")
def get_genre(db: Session = Depends(get_db)):
    q = db.query(MovieGenre).distinct().all()
    return q

@router.post("/genre")
def add_genre(genre_shema: MovieGenreSchema , db: Session = Depends(get_db)):

    

    query = select(MovieGenre.f_genre_id).order_by(MovieGenre.f_genre_id.desc()).limit(1)
    result = db.execute(query)

    # クエリ結果からf_movie_idを取得
    f_genre_id = result.scalar()

    try:
        new_f_genre_id = increment_f_genre_id(f_genre_id)
    except:
        new_f_genre_id = "G0000001"

    genre_shema.f_genre_id = new_f_genre_id

    genre = MovieGenre(**genre_shema.dict())
    db.add(genre)
    db.commit()
    db.refresh(genre)
    return {"msg": "success"}

def increment_f_genre_id(f_genre_id):
    # f_movie_idの現在の値を取得
    current_value = int(f_genre_id[2:])

    # f_movie_idをインクリメント
    incremented_value = current_value + 1

    # インクリメントされたf_movie_idをMG000001のような形式に変換
    new_f_movie_id = "G" + str(incremented_value).zfill(7)

    return new_f_movie_id