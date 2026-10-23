
from datetime import date
from enum import Enum
from uuid import UUID, uuid4

from sqlalchemy import Column, Enum as SQLAlchemyEnum
from sqlmodel import Field, SQLModel


class BookingStatus(str, Enum):
    PENDING = "pending"
    CONFIRMED = "confirmed"
    CANCELLED = "cancelled"


class Booking(SQLModel, table=True):
    id: UUID = Field(
        default_factory=uuid4,
        primary_key=True,
    )
    user_id: UUID
    resource_id: UUID
    reservation_date: date = Field(index=True)
    status: BookingStatus = Field(
        default=BookingStatus.PENDING,
        sa_column=Column(
            SQLAlchemyEnum(
                BookingStatus,
                name="bookingstatus",
                values_callable=lambda enum_cls: [
                    member.value for member in enum_cls
                ],
            ),
            nullable=False,
            server_default="pending",
        ),
    )
