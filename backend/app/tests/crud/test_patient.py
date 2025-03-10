
import uuid
from app.models import PatientCreate, PatientUpdate, UserCreate, PatientsPublic
from app.tests.utils.utils import random_email, random_lower_string, random_phone_number, rendom_patient
from sqlmodel import Session
from app import crud
from datetime import datetime



def test_patient(db: Session) -> None:
    user_in = UserCreate(email = random_email(), password = random_lower_string() )
    user = crud.create_user(session=db, user_create=user_in)
    patient = crud.create_patient(session=db, patient_create=rendom_patient() ,owner_id=user.id)
    # create patient test
    assert patient.owner_id == user.id
    patient1 = crud.create_patient(session=db, patient_create=rendom_patient() ,owner_id=user.id)
    for num in range(200):
        patient_rundom = crud.create_patient(session=db, patient_create=rendom_patient() ,owner_id=user.id)
        assert patient_rundom.id != patient1.id
    patients_found = crud.get_caregiver_patients(session=db, caregiver=user, skip=0, limit=100)
    assert type(patients_found) == PatientsPublic
    assert patients_found.count == 202
    updated_patient = PatientUpdate( 
        full_name="banana",
        email=random_email(), 
        phone_number=random_phone_number(), 
        height=1.1, 
        weight=1.1, 
        gender=2, 
        birth_date=datetime.now())
    updated_patient = crud.update_patient_info(session=db, db_patient=patient, patient_in=updated_patient)
    patient = crud.get_patient(session=db, id=updated_patient.id)
    # get patient by id + update patient test
    assert patient.full_name == "banana"
    



    