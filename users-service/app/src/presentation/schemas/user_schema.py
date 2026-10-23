from uuid import UUID
from sqlmodel import Field, SQLModel


class UserCreate(SQLModel):
    name: str = Field(min_length=1, max_length=100)
    last_name: str = Field(min_length=1, max_length=100)
    email: str = Field(min_length=5, max_length=255)
    identification_type: str = Field(min_length=1, max_length=30)
    identification_number: str = Field(min_length=1, max_length=50)


class UserRead(SQLModel):
    id: UUID
    name: str
    last_name: str
    email: str
    identification_type: str
    identification_number: str
