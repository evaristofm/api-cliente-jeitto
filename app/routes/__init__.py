from fastapi import APIRouter

from .cliente import router as cliente_router

main_router = APIRouter()

main_router.include_router(cliente_router, prefix="/cliente", tags=["cliente"])
