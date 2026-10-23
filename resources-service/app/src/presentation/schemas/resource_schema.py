from uuid import UUID
from sqlmodel import SQLModel


class ResourceCreate(SQLModel):
    """Datos necesarios para registrar un recurso."""

    name: str
    description: str | None = None
    location: str | None = None
    is_active: bool = True


class ResourceRead(SQLModel):
    """Datos que se devuelven al consultar un recurso."""

    id: UUID
    name: str
    description: str | None = None
    location: str | None = None
    is_active: bool
