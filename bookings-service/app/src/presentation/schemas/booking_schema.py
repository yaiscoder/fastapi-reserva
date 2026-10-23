from datetime import date
from uuid import UUID
from sqlmodel import SQLModel
from app.src.domain.models.booking_model import BookingStatus


class BookingCreate(SQLModel):
    user_id: UUID
    resource_id: UUID
    reservation_date: date


class BookingRead(SQLModel):
    id: UUID
    user_id: UUID
    resource_id: UUID
    reservation_date: date
    status: BookingStatus
