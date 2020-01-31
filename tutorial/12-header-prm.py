from typing import List

from fastapi import FastAPI, Header

app = FastAPI()

# to run server:
# `uvicorn 12-header-prm:app --reload`

# automatically convert underscores to hyphens
@app.get("/items-a/")
async def read_items(*, user_agent: str = Header(None)):
    return {"User-Agent": user_agent}

# do not convert underscores
@app.get("/items-b/")
async def read_items(*, strange_header: str = Header(None, convert_underscores=False)):
    return {"strange_header": strange_header}

# accept a list of items for a header
@app.get("/items-c/")
async def read_items(x_token: List[str] = Header(None)):
    return {"X-Token values": x_token}
