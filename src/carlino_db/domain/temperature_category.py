# src/carlino_db/domain/temperature_category.py

from enum import Enum


class TemperatureCategory(Enum):
    BELOW_38 = "<38°C"
    ABOVE_OR_EQUAL_38 = "≥38°C"
    NOT_PRESENT = "not_present"
