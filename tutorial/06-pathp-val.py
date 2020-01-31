
from fastapi import FastAPI, Path, Query

app = FastAPI()

# to run server:
# `uvicorn 06-pathp-val:app --reload`


@app.get("/items/{item_id}")
async def read_items(
    item_id: int = Path(..., title="The ID of the item to get"),
    q: str = Query(None, alias="item-query"),
):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    return results

# you can reorder args so that defaults come last
@app.get("/items-a/{item_id}")
async def read_items_a(
    q: str, item_id: int = Path(..., title="The ID of the item to get")
):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    return results

# trick for a different args order
@app.get("/items-b/{item_id}")
async def read_items_b(
    *, item_id: int = Path(..., title="The ID of the item to get"), q: str
):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    return results

# greater than or equal validation
@app.get("/items-c/{item_id}")
async def read_items_c(
    *, item_id: int = Path(..., title="The ID of the item to get", ge=1), q: str
):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    return results

# greather than or less than (or equal)
@app.get("/items-d/{item_id}")
async def read_items_d(
    *,
    item_id: int = Path(..., title="The ID of the item to get", gt=0, le=1000),
    q: str,
):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    return results


@app.get("/items-e/{item_id}")
async def read_items_e(
    *,
    item_id: int = Path(..., title="The ID of the item to get", ge=0, le=1000),
    q: str,
    size: float = Query(..., gt=0, lt=10.5)
):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    return results
