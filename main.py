from typing import List

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from models import SchoolInfo

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*']
)


@app.get("/search", response_model=List[SchoolInfo])
def search(q: str):
    return [{
        'name': "운정고등학교",
        'id': 1232,
        'address': '경기도 파주시 와석순환로 267',
        'classes': [12, 12, 12]
    }]
