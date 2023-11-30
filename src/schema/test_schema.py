from pydantic import BaseModel

class TestSchema(BaseModel):
    name: str
    fullname: str
    nickname: str

    class Config:
        orm_mode = True