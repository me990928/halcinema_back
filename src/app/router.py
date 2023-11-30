from fastapi import APIRouter
import sys
sys.path.append("../")
from api.v1 import info, movie, schedule, inquiry, test

api_router = APIRouter()

api_router.include_router(movie.router, prefix="/movie", tags=["movie"])
api_router.include_router(info.router, prefix="/info", tags=["info"])
api_router.include_router(schedule.router, prefix="/schedule", tags=["schedule"])
api_router.include_router(inquiry.router, prefix="/inquiry", tags=["inquiry"])
api_router.include_router(test.router, prefix="/test", tags=["test"])