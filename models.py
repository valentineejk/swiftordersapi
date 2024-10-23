from database import Base
from sqlalchemy import Boolean, Column, Integer, String
from pydantic import BaseModel

class Orders(BaseModel):
    # id: int
    coffee_name: str
    name: str
    size: str
    total: int

    # __tablename__ = 'orders'
    #
    # id = Column(Integer, primary_key=True, index=True)
    # coffee_name = Column(String, unique=True, index=True)
    # name = Column(String)
    # size = Column(String)
    # total = Column(Integer)
    # complete = Column(Boolean, default=False)


