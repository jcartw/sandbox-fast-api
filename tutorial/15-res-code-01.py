
from fastapi import FastAPI
from starlette.status import HTTP_201_CREATED


app = FastAPI()

# to run server:
# `uvicorn 15-res-code-01:app --reload`


@app.post("/items/", status_code=201)
async def create_item(name: str):
    return {"name": name}


@app.post("/items-a/", status_code=HTTP_201_CREATED)
async def create_item_a(name: str):
    return {"name": name}
