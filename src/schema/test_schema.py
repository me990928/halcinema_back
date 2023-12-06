from pydantic import BaseModel, ConfigDict

class TestSchema(BaseModel):
    name: str
    fullname: str
    nickname: str

    model_config = ConfigDict(from_attributes=True)