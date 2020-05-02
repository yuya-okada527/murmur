from fastapi import FastAPI
from pydantic import BaseModel

from typing import List
from datetime import datetime

app = FastAPI()


class Murmur(BaseModel):
    id: str
    user_id: str
    user_name: str
    message: str
    time: datetime


@app.get("/search/all_murmur", response_model=List[Murmur])
def search_all():
    return {"Hello": "World"}


@app.post("/regist/murmur")
def regist_murmur(murmur: Murmur):
    return murmur
