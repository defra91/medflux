# src/carlino_db/domain/family.py

from dataclasses import dataclass

from .child import Child
from .parent import Parent


@dataclass
class Family:
    id: str
    mother: Parent | None
    father: Parent | None

    children: list[Child]
