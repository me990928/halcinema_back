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

from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from starlette.requests import Request

@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    return JSONResponse(
        status_code=400,
        content={"detail": exc.errors(), "body": exc.body},
    )

app.include_router(api_router, prefix="/api/v1")