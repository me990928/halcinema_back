from fastapi import APIRouter

router = APIRouter()

@router.get("/", tags=["inquiry"])
def read_root():
    return {"root": "Inquiry API"}