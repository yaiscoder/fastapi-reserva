from abc import ABC, abstractmethod
from uuid import UUID
from app.src.domain.models.user_model import User


class UserRepository(ABC):
    """Contrato para las operaciones de persistencia de usuarios."""

    @abstractmethod
    def create(self, user: User) -> User:
        pass

    @abstractmethod
    def get_by_id(self, user_id: UUID) -> User | None:
        pass

    @abstractmethod
    def get_all(self) -> list[User]:
        pass