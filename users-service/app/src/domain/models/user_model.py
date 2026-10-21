from uuid import UUID, uuid4
from sqlmodel import Field, SQLModel


class User(SQLModel, table=True):
    id: UUID = Field(default_factory=uuid4,primary_key=True,)
    name: str = Field(index=True)
    last_name: str
    email: str = Field(unique=True)
    identification_type: str
    identification_number: str