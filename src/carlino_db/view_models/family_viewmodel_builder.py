# src/carlino_db/view_models/family_viewmodel_builder.py

from ..domain.family import Family
from .family_viewmodel import FamilyViewModel, FamilyViewModelComponent


def build_family_viewmodel(family: Family) -> FamilyViewModel:
    components: list[FamilyViewModelComponent] = []

    # Mother
    if family.mother:
        components.append(
            FamilyViewModelComponent(
                role="Mother",
            )
        )

    # Father
    if family.father:
        components.append(
            FamilyViewModelComponent(
                role="Father",
            )
        )

    # Children
    for _child in family.children:
        components.append(
            FamilyViewModelComponent(
                role="Child",
            )
        )

    return FamilyViewModel(
        id=family.id,
        components=components,
    )
