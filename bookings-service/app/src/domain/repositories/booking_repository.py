from abc import ABC, abstractmethod
from datetime import date
from uuid import UUID
from app.src.domain.models.booking_model import Booking


class BookingRepository(ABC):

    @abstractmethod
    def create(self, booking: Booking) -> Booking:
        pass

    @abstractmethod
    def get_by_id(self, booking_id: UUID) -> Booking | None:
        pass

    @abstractmethod
    def get_all(self) -> list[Booking]:
        pass

    @abstractmethod
    def get_by_date(self, reservation_date: date) -> list[Booking]:
        pass

    @abstractmethod
    def has_active_booking(
        self,
        resource_id: UUID,
        reservation_date: date,
    ) -> bool:
        pass

    @abstractmethod
    def update(self, booking: Booking) -> Booking:
        pass
