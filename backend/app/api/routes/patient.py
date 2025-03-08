import uuid
from typing import Any

from fastapi import APIRouter, HTTPException
from sqlmodel import func, select

from app.api.deps import CurrentPatient, SessionDep
from app.models import Patient, PatientCreate, PatientPublic, PatientsPublic, PatientUpdate

router = APIRouter(prefix="/items", tags=["items"])


@router.get("/", response_model=PatientsPublic)
def read_items(
    session: SessionDep, current_patient: CurrentPatient, skip: int = 0, limit: int = 100
) -> Any:
    """
    Retrieve items.
    """

    if current_patient.is_superuser:
        count_statement = select(func.count()).select_from(Patient)
        count = session.exec(count_statement).one()
        statement = select(Patient).offset(skip).limit(limit)
        patient = session.exec(statement).all()
    else:
        count_statement = (
            select(func.count())
            .select_from(patient)
            .where(patient.owner_id == current_patient.id)
        )
        count = session.exec(count_statement).one()
        statement = (
            select(patient)
            .where(patient.owner_id == current_patient.id)
            .offset(skip)
            .limit(limit)
        )
        items = session.exec(statement).all()

    return PatientPublic(data=items, count=count)


@router.get("/{id}", response_model=ItemPublic)
def read_item(session: SessionDep, current_user: CurrentUser, id: uuid.UUID) -> Any:
    """
    Get item by ID.
    """
    item = session.get(Item, id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    if not current_user.is_superuser and (item.owner_id != current_user.id):
        raise HTTPException(status_code=400, detail="Not enough permissions")
    return item


@router.post("/", response_model=ItemPublic)
def create_item(
    *, session: SessionDep, current_user: CurrentUser, item_in: ItemCreate
) -> Any:
    """
    Create new item.
    """
    item = Item.model_validate(item_in, update={"owner_id": current_user.id})
    session.add(item)
    session.commit()
    session.refresh(item)
    return item


@router.put("/{id}", response_model=ItemPublic)
def update_item(
    *,
    session: SessionDep,
    current_user: CurrentUser,
    id: uuid.UUID,
    item_in: ItemUpdate,
) -> Any:
    """
    Update an item.
    """
    item = session.get(Item, id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    if not current_user.is_superuser and (item.owner_id != current_user.id):
        raise HTTPException(status_code=400, detail="Not enough permissions")
    update_dict = item_in.model_dump(exclude_unset=True)
    item.sqlmodel_update(update_dict)
    session.add(item)
    session.commit()
    session.refresh(item)
    return item


@router.delete("/{id}")
def delete_item(
    session: SessionDep, current_user: CurrentUser, id: uuid.UUID
) -> Message:
    """
    Delete an item.
    """
    item = session.get(Item, id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    if not current_user.is_superuser and (item.owner_id != current_user.id):
        raise HTTPException(status_code=400, detail="Not enough permissions")
    session.delete(item)
    session.commit()
    return Message(message="Item deleted successfully")
