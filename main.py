
from fastapi import FastAPI, Depends, HTTPException, Path
from httpx import HTTPError
import models
from database import engine, SessionLocal
from typing import Annotated, List
from sqlalchemy.orm import Session
from models import Orders
from api import orders

app = FastAPI()
app.include_router(orders.router)
