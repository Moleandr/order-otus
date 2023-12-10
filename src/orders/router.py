from typing import Annotated

from pydantic import TypeAdapter
from sqlalchemy.exc import IntegrityError
from fastapi import APIRouter, Header, HTTPException

from src.dependencies import DBSession
from . import models
from . import schemas

router = APIRouter()


@router.get('/orders', response_model=list[schemas.OrderWithId])
def get_orders(session: DBSession):
    return TypeAdapter(list[schemas.OrderWithId]).validate_python(session.query(models.Order))


@router.post('/orders', response_model=schemas.OrderWithId)
def create_orders(
        session: DBSession,
        order_dto: schemas.Order,
        idempotency_key: Annotated[str | None, Header()]):
    try:
        with session.begin():
            session.add(models.Operation(
                id=idempotency_key
            ))
            order = models.Order(
                username=order_dto.username,
                items=order_dto.items
            )
            session.add(order)
            session.flush()
        return schemas.OrderWithId(
            id=order.id,
            username=order.username,
            items=order.items
        )
    except IntegrityError:
        raise HTTPException(status_code=409, detail="Idempotency key exists")
