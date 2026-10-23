from app.src.domain.models.booking_model import Booking, BookingStatus
from app.src.domain.repositories.booking_repository import BookingRepository


class BookingConflictError(Exception):
    """Se produce cuando la sala ya está reservada para esa fecha."""


class CreateBooking:

    def __init__(self, repository: BookingRepository):
        self.repository = repository

    def execute(self, booking: Booking) -> Booking:
        has_conflict = self.repository.has_active_booking(
            resource_id=booking.resource_id,
            reservation_date=booking.reservation_date,
        )

        if has_conflict:
            raise BookingConflictError(
                "La sala ya tiene una reserva activa para esa fecha."
            )

        booking.status = BookingStatus.PENDING

        return self.repository.create(booking)
