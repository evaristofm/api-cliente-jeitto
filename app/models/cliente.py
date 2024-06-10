from typing import Optional
from sqlmodel import Field, SQLModel


class Cliente(SQLModel, table=True):
    """Representa a tabela cliente no DB"""

    id: Optional[int] = Field(default=None, primary_key=True)
    email: str = Field(unique=True, nullable=False)
    username: str = Field(unique=True, nullable=False)
    phone: Optional[str] = Field(default=None, nullable=False)
