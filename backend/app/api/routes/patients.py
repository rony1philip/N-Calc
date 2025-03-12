import uuid


from app import crud
from fastapi import APIRouter, HTTPException
from sqlmodel import func, select

from app.api.deps import CurrentUser, SessionDep
from app.models import Patient, PatientCreate, PatientPublic, PatientsPublic, PatientUpdate, Message

router = APIRouter(prefix="/patients", tags=["patients"])


@router.get("/", response_model=PatientsPublic)
def read_patients(
    session: SessionDep, current_user: CurrentUser, 
) -> PatientsPublic:
   """
get patients of currentuser
    """
   patients =  crud.get_caregiver_patients(session=session,caregiver=current_user)
   return PatientsPublic(data=patients, count = len(patients))



@router.get("/{id}", response_model=PatientPublic)
def read_patient(session: SessionDep, current_user: CurrentUser,id:uuid.UUID) -> PatientPublic | None:
    """
    Get patient.
    """
    patient  = crud.get_patient(session=session,id=id)
    if current_user.id == patient.owner_id:
        return PatientPublic.form_patient(patient=patient)
    else:
        raise HTTPException(status_code=404, detail="Patient not found")
        


@router.post("/", response_model=PatientPublic)
def create_patient(
    *, session: SessionDep, current_user: CurrentUser, patient_in: PatientCreate
) -> PatientPublic:
    """
    Create new patient.
    """
    patient = crud.create_patient(session=session, patient_create=patient_in, owner_id=current_user.id)
    return PatientPublic.form_patient(patient=patient)

@router.put("/{id}", response_model=PatientPublic)
def update_patient(
    *,
    session: SessionDep, db_patient: Patient, patient_in: PatientUpdate,
) -> PatientPublic:
    patient = crud.update_patient_info(session=session,db_patient=db_patient,patient_in=patient_in )
    return PatientPublic.form_patient(patient=patient)


@router.delete("/{id}")
def delete_patient(
    session: SessionDep, current_user: CurrentUser, id: uuid.UUID
) -> Message:
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
    return Message(message=f"Patient deleted successfully - {id}")
