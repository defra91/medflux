# src/carlino_db/domain/family.py

from dataclasses import dataclass
from typing import Optional, List

from .parent import Parent
from .child import Child


@dataclass
class Family:
    id: str
    mother: Optional[Parent]
    father: Optional[Parent]

    children: list[Child]