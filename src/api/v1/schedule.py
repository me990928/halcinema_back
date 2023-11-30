from fastapi import APIRouter

router = APIRouter()

@router.get("/", tags=["schedule"])
def read_root():
    return {"root": "schedule API"}
