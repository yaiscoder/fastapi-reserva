from uuid import UUID
from app.src.domain.models.booking_model import Booking, BookingStatus
from app.src.domain.repositories.booking_repository import BookingRepository


class BookingNotFoundError(Exception):
    """La reserva solicitada no existe."""


class BookingAlreadyCancelledError(Exception):
    """La reserva ya se encuentra cancelada."""


class CancelBooking:

    def __init__(self, repository: BookingRepository):
        self.repository = repository

    def execute(self, booking_id: UUID) -> Booking:
        booking = self.repository.get_by_id(booking_id)

        if booking is None:
            raise BookingNotFoundError(
                "La reserva no existe."
            )

        if booking.status == BookingStatus.CANCELLED:
            raise BookingAlreadyCancelledError(
                "La reserva ya está cancelada."
            )

        booking.status = BookingStatus.CANCELLED

        return self.repository.update(booking)
