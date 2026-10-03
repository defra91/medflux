# src/medflux/domain/gender.py

from enum import Enum


class Gender(Enum):
    MALE = "Male"
    FEMALE = "Female"
    UNKNOWN = "Unknown"
