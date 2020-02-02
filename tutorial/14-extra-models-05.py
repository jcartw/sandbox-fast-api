
from typing import Dict

from fastapi import FastAPI

app = FastAPI()

# to run server:
# `uvicorn 14-extra-models-05:app --reload`


@app.get("/keyword-weights/", response_model=Dict[str, float])
async def read_keyword_weights():
    return {"foo": 2.3, "bar": 3.4}
