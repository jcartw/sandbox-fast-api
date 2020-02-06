
from fastapi import FastAPI, HTTPException

app = FastAPI()

# to run server:
# `uvicorn 19-error-handling-02:app --reload`

items = {"foo": "The Foo Wrestlers"}


@app.get("/items-header/{item_id}")
async def read_item_header(item_id: str):
    if item_id not in items:
        raise HTTPException(
            status_code=404,
            detail="Item not found",
            headers={"X-Error": "There goes my error"},
        )
    return {"item": items[item_id]}
