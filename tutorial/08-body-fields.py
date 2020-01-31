from fastapi import Body, FastAPI
from pydantic import BaseModel, Field

app = FastAPI()

# to run server:
# `uvicorn 08-body-fields:app --reload`


class Item(BaseModel):
    name: str
    description: str = Field(
        None, title="The description of the item", max_length=300)
    price: float = Field(..., gt=0,
                         description="The price must be greater than zero")
    tax: float = None


@app.put("/items-a/{item_id}")
async def update_item_a(*, item_id: int, item: Item = Body(..., embed=True)):
    results = {"item_id": item_id, "item": item}
    return results


@app.put("/items-b/{item_id}")
async def update_item_b(
    *,
    item_id: int,
    item: Item = Body(
        ...,
        example={
            "name": "Foo",
            "description": "A very nice Item",
            "price": 35.4,
            "tax": 3.2,
        },
    )
):
    results = {"item_id": item_id, "item": item}
    return results
