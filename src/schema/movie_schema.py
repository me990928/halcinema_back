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