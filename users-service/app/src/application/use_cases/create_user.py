from app.src.domain.models.user_model import User
from app.src.domain.repositories.user_repository import UserRepository


class CreateUser:
    """Caso de uso para registrar un usuario."""

    def __init__(self, repository: UserRepository):
        self.repository = repository

    def execute(self, user: User) -> User:
        return self.repository.create(user)
