# src/carlino_db/domain/family.py

from dataclasses import dataclass
from .parent import Parent
from .child import Child


@dataclass
class Family:
    family_id: str
    
    parents: list[Parent]
    children: list[Child]