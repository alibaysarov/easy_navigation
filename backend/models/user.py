from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Integer, Column
from uuid import UUID
from typing import Optional
from .base import Base


class User(Base):
    __tablename__ = "users"

    id: Mapped[UUID] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(80))
    email: Mapped[str] = mapped_column(String(80))
    password: Mapped[str] = mapped_column(String)
    bio: Mapped[Optional[str]] = mapped_column(String, nullable=True)
    age: Mapped[Optional[int]] = mapped_column(Integer, nullable=True)
    role = Column(String, default="user")

    def __repr__(self) -> str:
        return (
            f"User(id={self.id!r}, name={self.name!r}, "
            f"email={self.email!r}, password={self.password!r}, "
            f"bio={self.bio!r}, age={self.age!r})"
        )
