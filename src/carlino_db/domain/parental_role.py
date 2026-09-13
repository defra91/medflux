# src/carlino_db/domain/parental_role.py

from enum import Enum

class ParentalRole(str, Enum):
    """
    Enum representing the parental role of a parent.
    """
    MOTHER = "mother"
    FATHER = "father"
    UNKNOWN = "unknown"