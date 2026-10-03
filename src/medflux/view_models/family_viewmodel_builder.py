# src/medflux/view_models/family_viewmodel_builder.py

from ..domain.family import Family
from .child_symptoms_builder import build_child_symptoms
from .family_viewmodel import FamilyViewModel, FamilyViewModelComponent
from .parent_symptoms_builder import build_parent_symptoms


def build_family_viewmodel(family: Family) -> FamilyViewModel:
    components: list[FamilyViewModelComponent] = []

    # Mother
    if family.mother:
        components.append(
            FamilyViewModelComponent(
                role="Mother",
                mutation=family.mother.mutation,
                is_proband=False,
                symptoms=build_parent_symptoms(family.mother),
            )
        )

    # Father
    if family.father:
        components.append(
            FamilyViewModelComponent(
                role="Father",
                mutation=family.father.mutation,
                is_proband=False,
                symptoms=build_parent_symptoms(family.father),
            )
        )

    # Children
    for _child in family.children:
        components.append(
            FamilyViewModelComponent(
                role="Child", mutation=_child.mutation, is_proband=True, symptoms=build_child_symptoms(_child)
            )
        )

    return FamilyViewModel(
        id=family.id,
        components=components,
    )
