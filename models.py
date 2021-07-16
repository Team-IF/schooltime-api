from typing import List

from pydantic import BaseModel


class SchoolInfo(BaseModel):
    name: str
    id: int
    address: str
    classes: List[int]


class PeriodData(BaseModel):
    subject: str
    teacher: str
    changed: bool = False
