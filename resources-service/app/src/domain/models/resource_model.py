from uuid import UUID, uuid4
from sqlmodel import Field, SQLModel


class Resource(SQLModel, table=True):
    id: UUID = Field(default_factory=uuid4, primary_key=True)
    name: str = Field(index=True, min_length=1, max_length=100)
    description: str | None = Field(default=None, max_length=500)
    location: str | None = Field(default=None, max_length=150)
    is_active: bool = Field(default=True)
