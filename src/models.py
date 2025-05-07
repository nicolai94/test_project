from __future__ import annotations
from datetime import datetime
from advanced_alchemy.base import BigIntBase
from sqlalchemy import DateTime
from sqlalchemy.orm import Mapped, mapped_column


class User(BigIntBase):
    __tablename__ = "user"

    name: Mapped[str]
    surname: Mapped[str]
    password: Mapped[str]
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.now)
    updated_at: Mapped[datetime] = mapped_column(
        DateTime, default=datetime.now, onupdate=datetime.now
    )
