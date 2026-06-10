from services.point_import import PointImportService
from schemas.airport import Airport

import pytest

class FakeSession:
    async def execute(self, stmt):
        return None

@pytest.mark.asyncio
async def test_import():
    service = __get_service()

    airports = [
        Airport(name="АБАКАН", code="UNAA", lat="534424N", lng="0912307E")
    ]

    res, failed = await service.import_airport(airports)

    assert failed == 0
    assert len(res) == 1

def __get_service():
    db = FakeSession()
    service = PointImportService(db)
    return service