from fastapi import Cookie, FastAPI

app = FastAPI()

# to run server:
# `uvicorn 11-cookie-prm:app --reload`


@app.get("/items/")
async def read_items(*, ads_id: str = Cookie(None)):
    return {"ads_id": ads_id}
