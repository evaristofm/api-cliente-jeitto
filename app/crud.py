from sqlmodel import Session, select
from fastapi.exceptions import HTTPException

from app.models.cliente import Cliente
from app.models.serializer.cliente import ClienteRequest


def get_all_cliente(db: Session):
    return db.exec(select(Cliente)).all()


def get_cliente(db: Session, cliente_id: int):
    cliente_db = db.exec(select(Cliente).filter(Cliente.id == cliente_id)).first()
    if cliente_db is not None:
        return cliente_db
    raise HTTPException(status_code=404, detail='Cliente não encontrado.')


def create_cliente(db: Session, cliente: ClienteRequest):
    db_cliente = Cliente(**cliente.model_dump())

    db.add(db_cliente)
    db.commit()
    db.refresh(db_cliente)

    return db_cliente


def update_cliente(db: Session, cliente_id: int, cliente_request: ClienteRequest):
    cliente_db = db.exec(select(Cliente).filter(Cliente.id == cliente_id)).first()
    if cliente_db is None:
        raise HTTPException(status_code=404, detail='Cliente não encontrado.')

    cliente_db.username = cliente_request.username
    cliente_db.email = cliente_request.email
    cliente_db.phone = cliente_request.phone

    db.add(cliente_db)
    db.commit()
    return cliente_db


def delete_cliente(db: Session, cliente_id: int):
    cliente_db = db.exec(select(Cliente).filter(Cliente.id == cliente_id)).first()
    if cliente_db is None:
        raise HTTPException(status_code=404, detail='Cliente não encontrado.')

    db.delete(cliente_db)
    db.commit()

    return cliente_db
