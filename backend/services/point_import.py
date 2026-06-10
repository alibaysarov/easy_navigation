from schemas.airport import Airport
from decimal import Decimal
from helpers import get_decimal_from_degrees
import logging

logger = logging.getLogger(__name__)


class PointImportService:
    def import_airport(self, list: list[Airport]) -> tuple[list[dict], int]:
        result, failed = self.__prepare_arpts(list)
        logger.info("items %s", result)
        return result, failed

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
                    "lat": float(lat_decimal),
                    "lng": float(lng_decimal),
                    "elevation": 0.0,
                }
                result.append(item)
            except RuntimeError as e:
                failed += 1
        return result, failed
