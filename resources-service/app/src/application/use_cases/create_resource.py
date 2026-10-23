from app.src.domain.models.resource_model import Resource
from app.src.domain.repositories.resource_repository import ResourceRepository


class CreateResource:
    """Caso de uso para registrar un recurso."""

    def __init__(self, repository: ResourceRepository):
        self.repository = repository

    def execute(self, resource: Resource) -> Resource:
        return self.repository.create(resource)
