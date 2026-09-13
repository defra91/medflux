# src/carlino_db/domain/gender.py

from enum import Enum

class Gender(str, Enum):
    MALE = "Male"
    FEMALE = "Female"
    UNKNOWN = "Unknown"