from fastapi import APIRouter, Depends
import sys
sys.path.append("../../")
from schema.test_schema import TestSchema
from app.database import get_db
from typing import List
from sqlalchemy.orm import Session
from model.test import Test

router = APIRouter()

@router.post("/", tags=["test"])
def read_root():
    return {"root": "test API"}


@router.post("/create")
def read_root(test_schema: TestSchema, db: Session = Depends(get_db)):
    test = Test(**test_schema.dict())
    db.add(test)
    db.commit()
    db.refresh(test)
    return {"root": "test API"}