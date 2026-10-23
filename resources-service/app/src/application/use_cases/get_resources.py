from uuid import UUID
from app.src.domain.models.resource_model import Resource
from app.src.domain.repositories.resource_repository import ResourceRepository


class GetResources:
    """Casos de uso para consultar recursos."""

    def __init__(self, repository: ResourceRepository):
        self.repository = repository

    def execute(self) -> list[Resource]:
        return self.repository.get_all()

    def execute_by_id(self, resource_id: UUID) -> Resource | None:
        return self.repository.get_by_id(resource_id)
