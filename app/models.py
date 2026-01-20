from sqlalchemy import Column, String, Boolean, Enum, ForeignKey, DateTime, UniqueConstraint
from sqlalchemy.orm import relationship
from datetime import datetime
import enum
import uuid

from .database import Base

class ApplicationStatus(str, enum.Enum):
    APPLIED = "APPLIED"
    SHORTLISTED = "SHORTLISTED"
    REJECTED = "REJECTED"
    SELECTED = "SELECTED"


class Company(Base):
    __tablename__ = "companies"

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    name = Column(String, nullable=False)
    description = Column(String)


class Job(Base):
    __tablename__ = "jobs"

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    company_id = Column(String, ForeignKey("companies.id"))
    title = Column(String, nullable=False)
    description = Column(String)
    location = Column(String)
    is_active = Column(Boolean, default=True)


class Candidate(Base):
    __tablename__ = "candidates"

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    resume = Column(String)


class Application(Base):
    __tablename__ = "applications"

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    job_id = Column(String, ForeignKey("jobs.id"))
    candidate_id = Column(String, ForeignKey("candidates.id"))
    status = Column(Enum(ApplicationStatus), default=ApplicationStatus.APPLIED)
    applied_at = Column(DateTime, default=datetime.utcnow)

    __table_args__ = (
        UniqueConstraint("job_id", "candidate_id", name="unique_application"),
    )
