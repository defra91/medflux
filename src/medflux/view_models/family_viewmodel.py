from dataclasses import dataclass


@dataclass
class FamilyViewModelComponent:
    role: str
    mutation: str
    is_proband: bool
    symptoms: str


@dataclass
class FamilyViewModel:
    id: str
    components: list[FamilyViewModelComponent]
