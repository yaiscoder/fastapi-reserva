from datetime import date
from uuid import UUID
from app.src.domain.models.booking_model import Booking
from app.src.domain.repositories.booking_repository import BookingRepository


class GetBookings:

    def __init__(self, repository: BookingRepository):
        self.repository = repository

    def execute(self) -> list[Booking]:
        return self.repository.get_all()

    def execute_by_id(self, booking_id: UUID) -> Booking | None:
        return self.repository.get_by_id(booking_id)

    def execute_by_date(self, reservation_date: date) -> list[Booking]:
        return self.repository.get_by_date(reservation_date)
