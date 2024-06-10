from typing import List

from fastapi import APIRouter, Path, status
from sqlmodel import Session

from app import crud
from app.db import ActiveSession
from app.models.serializer.cliente import ClienteResponse, ClienteRequest


router = APIRouter()


@router.get("/", response_model=List[ClienteResponse], status_code=status.HTTP_200_OK)
async def get_all_clientes(*, session: Session = ActiveSession):
    """Busca todos os clientes"""
    clientes = crud.get_all_cliente(session)
    return clientes


@router.get("/{cliente_id}", response_model=ClienteResponse, status_code=status.HTTP_200_OK)
async def get_one_cliente(*, session: Session = ActiveSession, cliente_id: int):
    """Busca todos os clientes"""
    cliente = crud.get_cliente(session, cliente_id)
    return cliente


@router.post("/", response_model=ClienteResponse, status_code=status.HTTP_201_CREATED)
async def create_cliente(*, session: Session = ActiveSession, cliente_request: ClienteRequest):
    """Criar novos clientes"""
    db_cliente = crud.create_cliente(session, cliente_request)
    return db_cliente


@router.put("/{cliente_id}", status_code=status.HTTP_204_NO_CONTENT)
async def update_cliente(*,
                         session: Session = ActiveSession,
                         cliente_id: int = Path(gt=0),
                         cliente_request: ClienteRequest):
    """Atualizar clientes"""
    cliente_db = crud.update_cliente(session, cliente_id, cliente_request)
    return cliente_db


@router.delete("/{cliente_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_cliente(*, session: Session = ActiveSession, cliente_id: int = Path(gt=0)):
    """Excluir clientes"""
    cliente_model = crud.delete_cliente(session, cliente_id)
    return cliente_model

