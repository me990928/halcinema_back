from fastapi import APIRouter

router = APIRouter()

@router.get("/", tags=["info"])
def read_root():
    return {"root": "Info API"}