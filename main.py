from typing import List

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from models import SchoolInfo, PeriodData

app = FastAPI()

app.add_middleware(CORSMiddleware, allow_origins=["*"])


@app.get("/search", response_model=List[SchoolInfo])
def search(q: str):
    return [{"name": "운정고등학교", "id": 1232, "address": "경기도 파주시 와석순환로 267", "classes": [12, 12, 12]}]


@app.get("/timetable/{학교코드}/{학년}/{반}", response_model=List[List[PeriodData]])
def class_timetable(학교코드: int, 학년: int, 반: int):
    """
    반의 시간표를 가져옵니다
    """

    return [[{"subject": "수학", "teacher": "ㅁㄴㅇㄹ"}]]


@app.get("/timetable/{학교코드}/{학년}", response_model=List[List[List[PeriodData]]])
def grade_timetable(학교코드: int, 학년: int):
    """
    학년의 시간표를 가져옵니다
    """

    return [
        [[{"subject": "수학", "teacher": "ㅁㄴㅇㄹ"}]],
        [[{"subject": "수학", "teacher": "ㅁㄴㅇㄹ"}]],
    ]


@app.get("/timetable/{학교코드}", response_model=List[List[List[List[PeriodData]]]])
def school_timetable(학교코드: int):
    """
    학교의 시간표를 가져옵니다
    """

    return [
        [
            [[{"subject": "수학", "teacher": "ㅁㄴㅇㄹ"}]],
            [[{"subject": "수학", "teacher": "ㅁㄴㅇㄹ"}]],
        ],
        [
            [[{"subject": "수학", "teacher": "ㅁㄴㅇㄹ"}]],
            [[{"subject": "수학", "teacher": "ㅁㄴㅇㄹ"}]],
        ],
    ]
