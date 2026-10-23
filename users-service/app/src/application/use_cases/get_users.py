from uuid import UUID
from app.src.domain.models.user_model import User
from app.src.domain.repositories.user_repository import UserRepository


class GetUsers:
    """Casos de uso para consultar usuarios."""

    def __init__(self, repository: UserRepository):
        self.repository = repository

    def execute(self) -> list[User]:
        return self.repository.get_all()

    def execute_by_id(self, user_id: UUID) -> User | None:
        return self.repository.get_by_id(user_id)
