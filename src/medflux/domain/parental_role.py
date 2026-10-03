# src/medflux/domain/parental_role.py

from enum import Enum


class ParentalRole(Enum):
    """
    Enum representing the parental role of a parent.
    """

    MOTHER = "mother"
    FATHER = "father"
    UNKNOWN = "unknown"
