from sqlalchemy.orm import Session
from .models import *
from .exceptions import *

ALLOWED_TRANSITIONS = {
    ApplicationStatus.APPLIED: [ApplicationStatus.SHORTLISTED, ApplicationStatus.REJECTED],
    ApplicationStatus.SHORTLISTED: [ApplicationStatus.SELECTED, ApplicationStatus.REJECTED],
    ApplicationStatus.SELECTED: [],
    ApplicationStatus.REJECTED: []
}

def apply_to_job(db: Session, job_id: str, candidate_id: str):
    job = db.query(Job).filter(Job.id == job_id, Job.is_active == True).first()
    if not job:
        not_found("Job")

    exists = db.query(Application).filter_by(
        job_id=job_id, candidate_id=candidate_id
    ).first()

    if exists:
        duplicate_application()

    application = Application(job_id=job_id, candidate_id=candidate_id)
    db.add(application)
    db.commit()
    db.refresh(application)
    return application


def update_application_status(db: Session, application_id: str, new_status: ApplicationStatus):
    application = db.query(Application).filter_by(id=application_id).first()
    if not application:
        not_found("Application")

    if new_status not in ALLOWED_TRANSITIONS[application.status]:
        invalid_transition()

    application.status = new_status
    db.commit()
    return application
