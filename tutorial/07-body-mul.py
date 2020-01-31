
from fastapi import FastAPI, Path, Body
from pydantic import BaseModel

app = FastAPI()

# to run server:
# `uvicorn 07-body-mul:app --reload`


class Item(BaseModel):
    name: str
    description: str = None
    price: float
    tax: float = None


class User(BaseModel):
    username: str
    full_name: str = None

# make the body (i.e. item) optional by setting `item: Item = None`
@app.put("/items/{item_id}")
async def update_item(
    *,
    item_id: int = Path(..., title="The ID of the item to get", ge=0, le=1000),
    q: str = None,
    item: Item = None,
):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    if item:
        results.update({"item": item})
    return results


# accept both Item and User types in the req body
@app.put("/items-a/{item_id}")
async def update_item_a(*, item_id: int, item: Item, user: User):
    results = {"item_id": item_id, "item": item, "user": user}
    return results

# expected PUT req body
# {
#     "item": {
#         "name": "Foo",
#         "description": "The pretender",
#         "price": 42.0,
#         "tax": 3.2
#     },
#     "user": {
#         "username": "dave",
#         "full_name": "Dave Grohl"
#     }
# }

# add additional body param
@app.put("/items-b/{item_id}")
async def update_item_b(
    *,
    item_id: int,
    item: Item,
    user: User,
    importance: int = Body(..., gt=0),
    q: str = None
):
    results = {"item_id": item_id, "item": item,
               "user": user, "importance": importance}
    if q:
        results.update({"q": q})
    return results

# force object to be embedded in body via its key
@app.put("/items-c/{item_id}")
async def update_item_c(*, item_id: int, item: Item = Body(..., embed=True)):
    results = {"item_id": item_id, "item": item}
    return results
