import random
import string
from datetime import datetime
from app.models import PatientCreate
from fastapi.testclient import TestClient

from app.core.config import settings


def random_phone_number() -> str:
    return "".join(random.choices(string.digits, k=10))

def random_lower_string() -> str:
    return "".join(random.choices(string.ascii_lowercase, k=32))

def random_email() -> str:
    return f"{random_lower_string()}@{random_lower_string()}.com"

def rendom_patient()-> PatientCreate:
    return PatientCreate(
       full_name = random_lower_string(),
       email=random_email(), 
       phone_number=random_phone_number(), 
       height=random.random(), 
       weight=random.random(),
       gender= random.randint(a=1, b=3), 
       birth_date =  datetime.now()
    )

def get_superuser_token_headers(client: TestClient) -> dict[str, str]:
    login_data = {
        "username": settings.FIRST_SUPERUSER,
        "password": settings.FIRST_SUPERUSER_PASSWORD,
    }
    r = client.post(f"{settings.API_V1_STR}/login/access-token", data=login_data)
    tokens = r.json()
    a_token = tokens["access_token"]
    headers = {"Authorization": f"Bearer {a_token}"}
    return headers
