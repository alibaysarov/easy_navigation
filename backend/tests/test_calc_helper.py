import pytest
from helpers.math import get_decimal_from_degrees
from decimal import Decimal


def test_get_decimal_from_degrees():
    test_cases = [
        {
            "coord":"0731837E",
            "test_val":round(Decimal(73.31027778),4),
        },
        {
            "coord":"0731837W",
            "test_val":round(Decimal(-73.31027778),4),
        },
        {
            "coord":"1582702E",
            "test_val":round(Decimal(158.45055556),4)
        }
    ]
    
    for test in test_cases:
        assert get_decimal_from_degrees(test.get("coord")) == test.get("test_val")

def test_get_decimal_from_degrees_raises_exception():
    with pytest.raises(RuntimeError):
        get_decimal_from_degrees("0731837A")