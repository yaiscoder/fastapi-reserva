from uuid import UUID

from sqlmodel import Session, select

from app.src.domain.models.user_model import User
from app.src.domain.repositories.user_repository import UserRepository


class SQLModelUserRepository(UserRepository):
    """Implementación del repositorio usando SQLModel."""

    def __init__(self, session: Session):
        self.session = session

    def create(self, user: User) -> User:
        self.session.add(user)
        self.session.commit()
        self.session.refresh(user)
        return user

    def get_by_id(self, user_id: UUID) -> User | None:
        return self.session.get(User, user_id)

    def get_all(self) -> list[User]:
        statement = select(User)
        return list(self.session.exec(statement).all())
