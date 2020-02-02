
from typing import List

from fastapi import FastAPI
from pydantic import BaseModel, EmailStr

app = FastAPI()

# to run server:
# `uvicorn 13-resp-model:app --reload`


class Item(BaseModel):
    name: str
    description: str = None
    price: float
    tax: float = None
    tags: List[str] = []


class UserIn(BaseModel):
    username: str
    password: str
    email: EmailStr
    full_name: str = None


class UserOut(BaseModel):
    username: str
    email: EmailStr
    full_name: str = None


class Item2(BaseModel):
    name: str
    description: str = None
    price: float
    tax: float = 10.5
    tags: List[str] = []


class Item3(BaseModel):
    name: str
    description: str = None
    price: float
    tax: float = 10.5


items2 = {
    "foo": {"name": "Foo", "price": 50.2},
    "bar": {"name": "Bar", "description": "The bartenders", "price": 62, "tax": 20.2},
    "baz": {"name": "Baz", "description": None, "price": 50.2, "tax": 10.5, "tags": []},
}


@app.post("/items/", response_model=Item)
async def create_item(item: Item):
    return item

# Don't do this in production!
@app.post("/user/", response_model=UserOut)
async def create_user(*, user: UserIn):
    return user


@app.get("/items2/{item_id}", response_model=Item2, response_model_exclude_unset=True)
async def read_item2(item_id: str):
    return items2[item_id]

items3 = {
    "foo": {"name": "Foo", "price": 50.2},
    "bar": {"name": "Bar", "description": "The Bar fighters", "price": 62, "tax": 20.2},
    "baz": {
        "name": "Baz",
        "description": "There goes my baz",
        "price": 50.2,
        "tax": 10.5,
    },
}


@app.get(
    "/items3/{item_id}/name",
    response_model=Item3,
    response_model_include={"name", "description"},
)
async def read_item_name(item_id: str):
    return items3[item_id]


@app.get("/items3/{item_id}/public", response_model=Item3, response_model_exclude={"tax"})
async def read_item_public_data(item_id: str):
    return items3[item_id]
