from fastapi import HTTPException, status

def not_found(entity: str):
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"{entity} not found"
    )

def invalid_transition():
    raise HTTPException(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        detail="Invalid application status transition"
    )

def duplicate_application():
    raise HTTPException(
        status_code=status.HTTP_409_CONFLICT,
        detail="Candidate already applied to this job"
    )
