from typing import Annotated
from uuid import UUID
from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session
from app.src.application.use_cases.create_resource import CreateResource
from app.src.application.use_cases.get_resources import GetResources
from app.src.domain.models.resource_model import Resource
from app.src.infrastructure.database.session import get_session
from app.src.infrastructure.repositories.sqlmodel_resource_repository import (
    SQLModelResourceRepository,
)
from app.src.presentation.schemas.resource_schema import (
    ResourceCreate,
    ResourceRead,
)

router = APIRouter(prefix="/resources", tags=["Resources"])


@router.post(
    "/",
    response_model=ResourceRead,
    status_code=status.HTTP_201_CREATED,
)
def create_resource(
    resource_data: ResourceCreate,
    session: Annotated[Session, Depends(get_session)],
):
    repository = SQLModelResourceRepository(session)
    use_case = CreateResource(repository)

    resource = Resource(**resource_data.model_dump())
    return use_case.execute(resource)


@router.get("/", response_model=list[ResourceRead])
def get_resources(
    session: Annotated[Session, Depends(get_session)],
):
    repository = SQLModelResourceRepository(session)
    use_case = GetResources(repository)

    return use_case.execute()


@router.get("/{resource_id}", response_model=ResourceRead)
def get_resource_by_id(
    resource_id: UUID,
    session: Annotated[Session, Depends(get_session)],
):
    repository = SQLModelResourceRepository(session)
    use_case = GetResources(repository)

    resource = use_case.execute_by_id(resource_id)

    if resource is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Recurso no encontrado",
        )

    return resource
