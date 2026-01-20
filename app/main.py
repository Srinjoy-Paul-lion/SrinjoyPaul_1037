from fastapi import FastAPI, Depends, BackgroundTasks
from sqlalchemy.orm import Session

from .database import SessionLocal, engine
from .models import Base, ApplicationStatus
from .schemas import *
from .services import *

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Job Application Platform")


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def async_notification(app_id: str, status: str):
    print(f"[ASYNC] Application {app_id} updated to {status}")


@app.post("/companies")
def create_company(data: CompanyCreate, db: Session = Depends(get_db)):
    company = Company(**data.dict())
    db.add(company)
    db.commit()
    return company


@app.post("/companies/{company_id}/jobs")
def create_job(company_id: str, data: JobCreate, db: Session = Depends(get_db)):
    job = Job(company_id=company_id, **data.dict())
    db.add(job)
    db.commit()
    return job


@app.post("/candidates")
def create_candidate(data: CandidateCreate, db: Session = Depends(get_db)):
    candidate = Candidate(**data.dict())
    db.add(candidate)
    db.commit()
    return candidate


@app.post("/jobs/{job_id}/apply", response_model=ApplicationResponse)
def apply(job_id: str, data: ApplicationCreate, db: Session = Depends(get_db)):
    return apply_to_job(db, job_id, data.candidate_id)


@app.put("/applications/{application_id}/status")
def update_status(
    application_id: str,
    data: ApplicationStatusUpdate,
    background_tasks: BackgroundTasks,
    db: Session = Depends(get_db)
):
    application = update_application_status(
        db,
        application_id,
        ApplicationStatus(data.status)
    )

    background_tasks.add_task(
        async_notification, application.id, application.status
    )

    return {"message": "Status updated successfully"}
