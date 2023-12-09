from sqlalchemy import select
from sqlalchemy.orm import Session
from fastapi.params import Depends
import sys
sys.path.append("../")
from schema.movie_schema import MovieSchema, MovieTitleSchema
from model.m_movie_titles import MovieTitle
from app.database import get_db
from model.m_movies import Movie

def add_movie_title(movie_title_schema: MovieTitleSchema, db: Session = Depends(get_db)):
    
    # 再帰呼び出しの条件を追加する
    if movie_title_schema is None:
        return 0

    # f_movie_title_idを取得するクエリを作成
    query = select(MovieTitle.f_movie_title_id).order_by(MovieTitle.f_movie_title_id.desc()).limit(1)
    result = db.execute(query)

    # クエリ結果からf_movie_title_idを取得
    f_movie_title_id = result.scalar()

    try:
        new_f_movie_title_id = increment_f_movie_title_id(f_movie_title_id)
    except:
        new_f_movie_title_id = "MT000001"

    movie_title_schema.f_movie_title_id = new_f_movie_title_id

    movie_title = MovieTitle(**movie_title_schema.dict())
    db.add(movie_title)
    db.commit()
    db.refresh(movie_title)
    return new_f_movie_title_id

def increment_f_movie_title_id(f_movie_title_id):
    # f_movie_idの現在の値を取得
    current_value = int(f_movie_title_id[2:])

    # f_movie_idをインクリメント
    incremented_value = current_value + 1

    # インクリメントされたf_movie_idをMG000001のような形式に変換
    new_f_movie_title_id = "MT" + str(incremented_value).zfill(6)

    return new_f_movie_title_id