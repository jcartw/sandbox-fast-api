
from fastapi import FastAPI, File, UploadFile

app = FastAPI()

# to run server:
# `uvicorn 17-req-files-01:app --reload`


@app.post("/files/")
async def create_file(file: bytes = File(...)):
    return {"file_size": len(file)}


@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile = File(...)):
    return {"filename": file.filename}
