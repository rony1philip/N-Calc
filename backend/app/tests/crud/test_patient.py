
import uuid
from app.models import PatientCreate, UserCreate
from app.tests.utils.utils import random_email, random_lower_string, random_phone_number
from sqlmodel import Session
from datetime import datetime
from app import crud


def update_patient_info(db: Session) -> None:

    pass

def test_create_patient(db: Session) -> None:
    email = random_email()
    password = random_lower_string()
    user_in = UserCreate(email=email, password=password)
    user = crud.create_user(session=db, user_create=user_in)
    full_name = random_lower_string()
    patient_email = random_email()
    phone_number = random_phone_number()
    birth_date = datetime.now()
    height = 1.0
    weight =1.0 
    gender = 2
    patient_in = PatientCreate(full_name=full_name, email=patient_email, phone_number=phone_number, height=height, weight=weight, gender=gender, birth_date=birth_date)
    patient = crud.create_patient(session=db, patient_create=patient_in ,owner_id=user.id)
    assert patient_email == patient.email
    

def get_caregiver_patients():
    pass

def get_patient_by_email():
    pass