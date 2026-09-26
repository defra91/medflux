from dataclasses import dataclass


@dataclass
class FamilyViewModelComponent:
    role: str


@dataclass
class FamilyViewModel:
    id: str
    components: list[FamilyViewModelComponent]
