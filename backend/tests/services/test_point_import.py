from services.point_import import PointImportService
from schemas.airport import Airport

import pytest

def test_import():
    service = PointImportService()
    list = [
        Airport(name="АБАКАН",code="UNAA",lat="534424N",lng="0912307E")
    ]
    res,failed = service.import_airport(list)
    
    assert failed==0