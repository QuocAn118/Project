from pydantic import BaseModel
from typing import Optional, List
from enum import Enum

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: Optional[str] = None

class UserCreate(BaseModel):
    username: str
    full_name: Optional[str]
    password: str
    role: Optional[str] = "staff"
    department_id: Optional[int]

class UserOut(BaseModel):
    id: int
    username: str
    full_name: Optional[str]
    role: str
    department_id: Optional[int]
    kpi_score: float

    class Config:
        orm_mode = True

class WebhookMessage(BaseModel):
    platform: str
    sender: str
    content: str

class MessageOut(BaseModel):
    id: int
    platform: str
    sender: str
    content: str
    keywords: Optional[str]

    class Config:
        orm_mode = True

class DepartmentOut(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True

class KeywordCreate(BaseModel):
    word: str
    department_id: Optional[int]

class KeywordOut(BaseModel):
    id: int
    word: str
    department_id: Optional[int]

    class Config:
        orm_mode = True

class AssignmentOut(BaseModel):
    id: int
    message_id: int
    user_id: int
    status: str

    class Config:
        orm_mode = True

class ReportQuery(BaseModel):
    start: Optional[str]
    end: Optional[str]
    group_by: Optional[str] = "department"

class RequestCreate(BaseModel):
    request_type: str  # leave or raise
    description: str

class RequestOut(BaseModel):
    id: int
    user_id: int
    request_type: str
    description: str
    status: str
    submitted_at: str

    class Config:
        orm_mode = True

class RequestReview(BaseModel):
    status: str  # approved or rejected
    notes: Optional[str]

class ShiftOut(BaseModel):
    id: int
    shift_name: str
    start_time: str
    end_time: str

    class Config:
        orm_mode = True

class ShiftAssignmentCreate(BaseModel):
    user_id: int
    shift_id: int
    assigned_date: str

class TimeTrackingOut(BaseModel):
    id: int
    user_id: int
    check_in_time: Optional[str]
    check_out_time: Optional[str]
    date: str

    class Config:
        orm_mode = True

class KPIMetricOut(BaseModel):
    user_id: int
    metric_name: str
    metric_value: float
    period: str

    class Config:
        orm_mode = True
