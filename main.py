from fastapi import FastAPI
from fastapi import File
from fastapi import UploadFile
from fastapi import Form

from typing import Annotated

app = FastAPI()

# Import File and Form
@app.post("/files")
async def create_file(
  file: Annotated[bytes, File()],
  fileb: Annotated[UploadFile, File()],
  token: Annotated[str, Form()]
):
  return {
    "file_size": len(file),
    "fileb_content_type": fileb.content_type,
    "token": token
  }
