from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session  # type: ignore

from . import crud, models
from .database import SessionLocal, engine
from .schemas import ItemBase

models.Base.metadata.create_all(bind=engine)
itemrouter = APIRouter()