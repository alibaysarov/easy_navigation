from .base import Base
from sqlalchemy import UUID, Column, String, Float
from sqlalchemy.orm import Mapped, mapped_column
from geoalchemy2 import Geometry


class Airport(Base):
    __tablename__ = "airports"

    id: Mapped[UUID] = mapped_column(UUID, primary_key=True)

    name: Mapped[String] = mapped_column(String, nullable=False)

    icao_code = Column(String, nullable=False, unique=True)

    coordinates: Mapped[Geometry] = mapped_column(
        Geometry(geometry_type="POINT", srid=4326)
    )

    elevation = Column(Float, nullable=False)
