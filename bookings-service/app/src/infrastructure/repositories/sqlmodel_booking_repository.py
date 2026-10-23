from datetime import date
from uuid import UUID
from sqlmodel import Session, select
from app.src.domain.models.booking_model import Booking, BookingStatus
from app.src.domain.repositories.booking_repository import BookingRepository


class SQLModelBookingRepository(BookingRepository):

    def __init__(self, session: Session):
        self.session = session

    def create(self, booking: Booking) -> Booking:
        self.session.add(booking)
        self.session.commit()
        self.session.refresh(booking)
        return booking

    def get_by_id(self, booking_id: UUID) -> Booking | None:
        return self.session.get(Booking, booking_id)

    def get_all(self) -> list[Booking]:
        statement = select(Booking)
        return list(self.session.exec(statement).all())

    def get_by_date(self, reservation_date: date) -> list[Booking]:
        statement = select(Booking).where(
            Booking.reservation_date == reservation_date
        )
        return list(self.session.exec(statement).all())

    def has_active_booking(
        self,
        resource_id: UUID,
        reservation_date: date,
    ) -> bool:
        statement = select(Booking).where(
            Booking.resource_id == resource_id,
            Booking.reservation_date == reservation_date,
            Booking.status != BookingStatus.CANCELLED,
        )
        return self.session.exec(statement).first() is not None

    def update(self, booking: Booking) -> Booking:
        self.session.add(booking)
        self.session.commit()
        self.session.refresh(booking)
        return booking
