from typing import List

import fastapi
from fastapi import Path

from models import Orders

router = fastapi.APIRouter()

# models.Base.metadata.create_all(bind=engine)

orders = []

# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()

# db_dependency = Annotated[Session, Depends(get_db)]

@router.get("/")
async def read_root():
    return {"Hello": "World"}


@router.get("/orders", response_model=List[Orders])
async def get_orders():
    return orders

@router.post("/orders")
async def add_orders(order: Orders):
    orders.append(order)
    return {"status": True}

@router.get("/orders/{id}")
async def get_order(id: int = Path(..., description="The ID of the user, you want to retrieve", gt=2)):
    return orders[id]
