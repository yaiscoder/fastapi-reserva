from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session
from uuid import UUID
from app.src.application.use_cases.create_user import CreateUser
from app.src.application.use_cases.get_users import GetUsers
from app.src.domain.models.user_model import User
from app.src.infrastructure.database.session import get_session
from app.src.infrastructure.repositories.sqlmodel_user_repository import (
    SQLModelUserRepository,
)
from app.src.presentation.schemas.user_schema import UserCreate, UserRead
from sqlalchemy.exc import IntegrityError

router = APIRouter(prefix="/users", tags=["Users"])


@router.post(
    "/",
    response_model=UserRead,
    status_code=status.HTTP_201_CREATED,
)
def create_user(
    user_data: UserCreate,
    session: Session = Depends(get_session),
):
    repository = SQLModelUserRepository(session)
    use_case = CreateUser(repository)

    user = User.model_validate(user_data)
    
    try:
        return use_case.execute(user)
    except IntegrityError as exc:
        session.rollback()
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="El correo o algún otro dato único ya está registrado.",
        ) from exc


@router.get("/", response_model=list[UserRead])
def get_users(session: Session = Depends(get_session)):
    repository = SQLModelUserRepository(session)
    use_case = GetUsers(repository)
    return use_case.execute()


@router.get("/{user_id}", response_model=UserRead)
def get_user(
    user_id: UUID,
    session: Session = Depends(get_session),
):
    repository = SQLModelUserRepository(session)
    user = GetUsers(repository).execute_by_id(user_id)

    if user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Usuario no encontrado",
        )

    return user
