
from typing import List

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# to run server:
# `uvicorn 14-extra-models-04:app --reload`


class Item(BaseModel):
    name: str
    description: str


items = [
    {"name": "Foo", "description": "There comes my hero"},
    {"name": "Red", "description": "It's my aeroplane"},
]


@app.get("/items/", response_model=List[Item])
async def read_items():
    return items
