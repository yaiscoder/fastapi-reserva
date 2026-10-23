from typing import Annotated
from uuid import UUID
from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session

from app.src.application.use_cases.create_booking import (
    BookingConflictError,
    CreateBooking,
)
from app.src.application.use_cases.get_bookings import GetBookings
from app.src.domain.models.booking_model import Booking
from app.src.infrastructure.database.session import get_session
from app.src.infrastructure.repositories.sqlmodel_booking_repository import (
    SQLModelBookingRepository,
)
from app.src.presentation.schemas.booking_schema import (
    BookingCreate,
    BookingRead,
)

router = APIRouter(prefix="/bookings", tags=["Bookings"])


@router.post(
    "/",
    response_model=BookingRead,
    status_code=status.HTTP_201_CREATED,
)
def create_booking(
    booking_data: BookingCreate,
    session: Annotated[Session, Depends(get_session)],
):
    repository = SQLModelBookingRepository(session)
    use_case = CreateBooking(repository)

    booking = Booking(
        user_id=booking_data.user_id,
        resource_id=booking_data.resource_id,
        reservation_date=booking_data.reservation_date,
    )

    try:
        return use_case.execute(booking)
    except BookingConflictError as error:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=str(error),
        ) from error


@router.get("/", response_model=list[BookingRead])
def get_bookings(
    session: Annotated[Session, Depends(get_session)],
):
    repository = SQLModelBookingRepository(session)
    use_case = GetBookings(repository)
    return use_case.execute()


@router.get("/{booking_id}", response_model=BookingRead)
def get_booking_by_id(
    booking_id: UUID,
    session: Annotated[Session, Depends(get_session)],
):
    repository = SQLModelBookingRepository(session)
    use_case = GetBookings(repository)

    booking = use_case.execute_by_id(booking_id)

    if booking is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Reserva no encontrada",
        )

    return booking
