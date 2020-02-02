
from fastapi import FastAPI, Form

app = FastAPI()

# to run server:
# `uvicorn 16-form-data-01:app --reload`


@app.post("/login/")
async def login(*, username: str = Form(...), password: str = Form(...)):
    return {"username": username}
