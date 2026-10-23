from uuid import UUID
from sqlmodel import Session, select
from app.src.domain.models.resource_model import Resource
from app.src.domain.repositories.resource_repository import ResourceRepository


class SQLModelResourceRepository(ResourceRepository):
    """Implementación del repositorio usando SQLModel."""

    def __init__(self, session: Session):
        self.session = session

    def create(self, resource: Resource) -> Resource:
        self.session.add(resource)
        self.session.commit()
        self.session.refresh(resource)
        return resource

    def get_by_id(self, resource_id: UUID) -> Resource | None:
        return self.session.get(Resource, resource_id)

    def get_all(self) -> list[Resource]:
        statement = select(Resource)
        return list(self.session.exec(statement).all())
