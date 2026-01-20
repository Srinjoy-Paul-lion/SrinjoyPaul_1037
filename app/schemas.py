from pydantic import BaseModel, EmailStr
from enum import Enum
from datetime import datetime

class CompanyCreate(BaseModel):
    name: str
    description: str | None = None


class JobCreate(BaseModel):
    title: str
    description: str
    location: str
    is_active: bool = True


class CandidateCreate(BaseModel):
    name: str
    email: EmailStr
    resume: str


class ApplicationCreate(BaseModel):
    candidate_id: str


class ApplicationStatusUpdate(BaseModel):
    status: str


class ApplicationResponse(BaseModel):
    id: str
    job_id: str
    candidate_id: str
    status: str
    applied_at: datetime
