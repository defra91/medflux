# src/carlino_db/domain/parent.py

from dataclasses import dataclass
from .parental_role import ParentalRole

@dataclass
class Parent:

    family_id: str
    parental_role: ParentalRole