from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from router import api_router

app = FastAPI(
    title="HALCINEMA API",
    )

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # localhostの許可
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(api_router, prefix="/api/v1")