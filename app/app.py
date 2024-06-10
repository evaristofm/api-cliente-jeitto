from fastapi import FastAPI

from .routes import main_router


app = FastAPI(
    title="Clientes",
    version="0.1.0",
    description="Api cadastro de clientes"
)

app.include_router(main_router)
