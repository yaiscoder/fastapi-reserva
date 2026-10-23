from abc import ABC, abstractmethod
from uuid import UUID
from app.src.domain.models.resource_model import Resource


class ResourceRepository(ABC):
    """Contrato para las operaciones sobre recursos."""

    @abstractmethod
    def create(self, resource: Resource) -> Resource:
        pass

    @abstractmethod
    def get_by_id(self, resource_id: UUID) -> Resource | None:
        pass

    @abstractmethod
    def get_all(self) -> list[Resource]:
        pass
