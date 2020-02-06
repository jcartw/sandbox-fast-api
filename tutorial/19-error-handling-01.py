
from fastapi import FastAPI, HTTPException

app = FastAPI()

# to run server:
# `uvicorn 19-error-handling-01:app --reload`

items = {"foo": "The Foo Wrestlers"}


@app.get("/items/{item_id}")
async def read_item(item_id: str):
    if item_id not in items:
        raise HTTPException(status_code=404, detail="Item not found")
    return {"item": items[item_id]}
