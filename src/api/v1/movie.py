from fastapi import APIRouter

router = APIRouter()

@router.get("/", tags=["movie"])
def read_root():
    return {"root": "Movie API"}