
import uuid
from app.models import PatientCreate, PatientUpdate, UserCreate
from app.tests.utils.utils import random_email, random_lower_string, random_phone_number
from sqlmodel import Session
from datetime import datetime
from app import crud




def test_patient(db: Session) -> None:
    user_in = UserCreate(email = random_email(), password = random_lower_string() )
    user = crud.create_user(session=db, user_create=user_in)
    gender=2
    patient_in = PatientCreate(
        full_name=random_lower_string(),
        email=random_email(), 
        phone_number=random_phone_number(), 
        height=1.1, 
        weight=1.1, 
        gender=gender, 
        birth_date=datetime.now())
    patient = crud.create_patient(session=db, patient_create=patient_in ,owner_id=user.id)
    # create patient test
    assert patient.gender == 2
    assert patient.owner_id == user.id
    patient_in2 =  PatientCreate(
        full_name=random_lower_string(),
        email="blabla@gmail.com", 
        phone_number=random_phone_number(), 
        height=1.1, 
        weight=1.1, 
        gender=1, 
        birth_date=datetime.now())
    patient2 = crud.create_patient(session=db, patient_create=patient_in2 ,owner_id=user.id)
    caregiver_patients = crud.get_caregiver_patients(session=db, caregiver=user)
    # get patients test
    assert patient.owner_id == patient2.owner_id
    assert caregiver_patients.count == 2
    updated_patient = PatientUpdate( 
        full_name="banana",
        email=random_email(), 
        phone_number=random_phone_number(), 
        height=1.1, 
        weight=1.1, 
        gender=2, 
        birth_date=datetime.now())
    updated_patient = crud.update_patient_info(session=db, db_patient=patient, patient_in=updated_patient)
    # update patient test
    assert updated_patient.full_name == "banana"
    patient = crud.get_patient(session=db, id=updated_patient.id)
    # get patient by email
    assert patient.full_name == "banana"
    



    