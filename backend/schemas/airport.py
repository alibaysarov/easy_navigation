from pydantic import BaseModel, Field, field_validator

"""
 "name": "АБАКАН",
        "code": "UNAA",
        "lat": "534424N",
        "lng": "0912307E"
"""

_regex_coord = r"\d{6,7}[NESW]"


class Airport(BaseModel):
    name: str
    code: str
    lat: str
    lng: str

    @field_validator("lat", "lng")
    @classmethod
    def normalize(cls, v: str):
        return v.replace("Е", "E").replace("С", "S").replace("В", "E").replace("З", "W")
