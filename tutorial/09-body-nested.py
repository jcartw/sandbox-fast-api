from typing import List, Set, Dict

from fastapi import FastAPI
from pydantic import BaseModel, HttpUrl

app = FastAPI()

# to run server:
# `uvicorn 09-body-nested:app --reload`


class Item(BaseModel):
    name: str
    description: str = None
    price: float
    tax: float = None
    tags: List[str] = []  # specify that this must be a list of strings


class Item2(BaseModel):
    name: str
    description: str = None
    price: float
    tax: float = None
    tags: Set[str] = set()


class Image(BaseModel):
    url: HttpUrl
    name: str


class Item3(BaseModel):
    name: str
    description: str = None
    price: float
    tax: float = None
    tags: Set[str] = []
    image: Image = None
    images: List[Image] = None


class Offer(BaseModel):
    name: str
    description: str = None
    price: float
    items: List[Item]


@app.put("/items-a/{item_id}")
async def update_item_a(*, item_id: int, item: Item):
    results = {"item_id": item_id, "item": item}
    return results


@app.put("/items-b/{item_id}")
async def update_item_b(*, item_id: int, item2: Item2):
    results = {"item_id": item_id, "item2": item2}
    return results


@app.put("/items-c/{item_id}")
async def update_item_c(*, item_id: int, item3: Item3):
    results = {"item_id": item_id, "item3": item3}
    return results


@app.post("/offers/")
async def create_offer(*, offer: Offer):
    return offer


@app.post("/images/multiple/")
async def create_multiple_images(*, images: List[Image]):
    return images


@app.post("/index-weights/")
async def create_index_weights(weights: Dict[int, float]):
    return weights
