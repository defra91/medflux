# src/medflux/domain/family.py

from dataclasses import dataclass

from .child import Child
from .parent import Parent


@dataclass
class Family:
    id: str
    mother: Parent | None
    father: Parent | None

    children: list[Child]

    def parents(self) -> list[Parent]:
        result = []
        if self.mother is not None:
            result.append(self.mother)
        if self.father is not None:
            result.append(self.father)
        return result
