from schemas.airport import Airport
from sqlalchemy import text
from geoalchemy2 import WKTElement

from sqlalchemy.dialects.postgresql import insert
from sqlalchemy.orm import Session
from helpers import get_decimal_from_degrees
import logging
from models.airport import Airport as AirportModel

logger = logging.getLogger(__name__)


class PointImportService:
    
    def __init__(self,db:Session):
        self.db = db
        
    
    async def import_airport(self, list: list[Airport]) -> tuple[list[dict], int]:
        result, failed = self.__prepare_arpts(list)
        
        await self.db.execute(text("SET TRANSACTION ISOLATION LEVEL REPEATABLE READ"))

        stmt = insert(AirportModel).values(result)

        stmt = stmt.on_conflict_do_update(
            index_elements=["icao_code"],
            set_={
                "name": stmt.excluded.name,
                "icao_code":stmt.excluded.icao_code,
                "coordinates": stmt.excluded.coordinates,
                "elevation": stmt.excluded.elevation,
            },
        )

        await self.db.execute(stmt)
        
        response_result = [
            {
                "name": item["name"],
                "icao_code": item["icao_code"],
                "elevation": item["elevation"],
            }
            for item in result
        ]
        return response_result, failed

    def __prepare_arpts(self, list: list[Airport]) -> tuple[list[dict], int]:
        result = []
        failed = 0
        for airport in list:
            try:
                lat_decimal = get_decimal_from_degrees(airport.lat)
                lng_decimal = get_decimal_from_degrees(airport.lng)

                item = {
                    "name": airport.name,
                    "icao_code": airport.code.upper(),
                    "coordinates": WKTElement(
                            f"POINT({float(lng_decimal)} {float(lat_decimal)})",
                            srid=4326,
                        ),
                    "elevation": 0.0,
                }
                result.append(item)
            except RuntimeError as e:
                failed += 1
        return result, failed
