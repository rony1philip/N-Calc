import uuid
from typing import Any

from app import crud
from fastapi import APIRouter, HTTPException
from sqlmodel import func, select

from app.api.deps import CurrentUser, SessionDep
from app.models import Patient, PatientCreate, PatientPublic, PatientsPublic, PatientUpdate, Message

router = APIRouter(prefix="/patients", tags=["patients"])


@router.get("/", response_model=PatientsPublic)
def read_patients(
    session: SessionDep, current_user: CurrentUser, skip: int = 0, limit: int = 100
) -> Any:
   """
get patients of currentuser
    """
   patients =  crud.get_caregiver_patients(session=session,caregiver=current_user)
   return PatientsPublic(data=patients, count = len(patients))



@router.get("/{id}", response_model=PatientPublic)
def read_patient(session: SessionDep, current_user: CurrentUser,id:uuid.UUID) -> Any:
    """
    Get patient.
    """
    patient  = crud.get_patient(session=session,id=id)
    return PatientPublic(
        full_name=patient.full_name,
        description=patient.description,
        email=patient.email,
        phone_number=patient.phone_number,
        height=patient.height, 
        weight=patient.weight, 
        gender=patient.gender, 
        birth_date=patient.birth_date, 
        owner_id=patient.owner_id, 
        id=patient.id
    )


@router.post("/", response_model=PatientPublic)
def create_patient(
    *, session: SessionDep, current_user: CurrentUser, patient_in: PatientCreate
) -> Any:
    """
    Create new patient.
    """
    patient = crud.create_patient(session=session, patient_create=patient_in, owner_id=current_user.id)
    return PatientPublic(
        full_name=patient.full_name,
        description=patient.description,
        email=patient.email,
        phone_number=patient.phone_number,
        height=patient.height, 
        weight=patient.weight, 
        gender=patient.gender, 
        birth_date=patient.birth_date, 
        owner_id=patient.owner_id, 
        id=patient.id
    )

@router.put("/{id}", response_model=PatientPublic)
def update_patient(
    *,
    session: SessionDep, db_patient: Patient, patient_in: PatientUpdate,
) -> Any:
    patient = crud.update_patient_info(session=session,db_patient=db_patient,patient_in=patient_in )
    return PatientPublic(
        full_name=patient.full_name,
        description=patient.description,
        email=patient.email,
        phone_number=patient.phone_number,
        height=patient.height, 
        weight=patient.weight, 
        gender=patient.gender, 
        birth_date=patient.birth_date, 
        owner_id=patient.owner_id, 
        id=patient.id
    )


@router.delete("/{id}")
def delete_patient(
    session: SessionDep, current_user: CurrentUser, id: uuid.UUID
) -> Any:
    """
    Delete an Patient.
    """
    patient = session.get(Patient, id)
    if not patient:
        raise HTTPException(status_code=404, detail="Patient not found")
    if not current_user.is_superuser and (patient.owner_id != current_user.id):
        raise HTTPException(status_code=400, detail="Not enough permissions")
    session.delete(patient)
    session.commit()
    return Message(message="Patient deleted successfully")
