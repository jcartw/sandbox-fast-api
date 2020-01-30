
from fastapi import FastAPI

app = FastAPI()

# to run server:
# `uvicorn 01-first_steps:app --reload`

@app.get("/")
async def root():
    return {"message": "Hello World"}