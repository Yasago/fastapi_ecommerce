from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from app.backend.db import Base


class User(Base):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(
        primary_key=True,
        index=True
    )

    first_name: Mapped[str] = mapped_column(String)
    last_name: Mapped[str] = mapped_column(String)

    username: Mapped[str] = mapped_column(
        String,
        unique=True
    )

    email: Mapped[str] = mapped_column(
        String,
        unique=True
    )

    hashed_password: Mapped[str] = mapped_column(String)

    is_active: Mapped[bool] = mapped_column(default=True)
    is_admin: Mapped[bool] = mapped_column(default=False)
    is_supplier: Mapped[bool] = mapped_column(default=False)
    is_customer: Mapped[bool] = mapped_column(default=True)
