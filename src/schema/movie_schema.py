from pydantic import BaseModel, ConfigDict
from datetime import datetime as DateTime

class MovieSchema(BaseModel):
    f_movie_id: str | None = None
    f_movie_title_id: str
    f_genre_id: str
    f_content: str
    f_movie_runtime_min: int
    f_movie_data: str
    model_config = ConfigDict(from_attributes=True)


class MovieTitleSchema(BaseModel):
    f_movie_title_id: str | None = None
    f_movie_title_japan: str
    f_movie_title_foreign: str
    model_config = ConfigDict(from_attributes=True)

class MoviePictSchema(BaseModel):
    f_movie_pict_id: int | None = None
    f_movie_id: str
    f_movie_pict: str
    model_config = ConfigDict(from_attributes=True)

class MovieGenreSchema(BaseModel):
    f_genre_id: str | None = None
    f_genre_name: str
    model_config = ConfigDict(from_attributes=True)