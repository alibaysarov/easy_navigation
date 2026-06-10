from decimal import Decimal


K = {"N": +1, "S": -1, "W": -1, "E": +1}


def get_decimal_from_degrees(degree: str):
    last = degree[-1].upper()

    if K.get(last) is None:
        raise RuntimeError("No Valid Hemisphere provided")

    numbers = degree[:-1].rjust(7, "0")

    degrees = int(numbers[0:3])
    mins = int(numbers[3:5])
    seconds = int(numbers[5:7])

    result = Decimal(degrees) + Decimal(mins / 60) + Decimal(seconds / 3600)
    return round(result * K[last], 4)
