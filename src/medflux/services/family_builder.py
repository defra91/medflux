from ..domain.child import Child
from ..domain.family import Family
from ..domain.parent import Parent, ParentalRole


def build_families(children: list[Child], parents: list[Parent]) -> list[Family]:
    """
    Builds a list of Family objects from lists of Child and Parent objects.
    """
    parents_by_family = _group_parents_by_family(parents)
    children_by_family = _group_children_by_family(children)

    families: list[Family] = []

    # Unione delle chiavi: alcune famiglie potrebbero avere solo parent o solo children
    all_family_ids = set(parents_by_family.keys()) | set(children_by_family.keys())

    for family_id in sorted(all_family_ids):
        mother, father = _extract_mother_father(parents_by_family.get(family_id, []))
        family_children = children_by_family.get(family_id, [])

        family = _build_single_family(family_id=family_id, mother=mother, father=father, children=family_children)

        families.append(family)

    return families


# ---------------------------------------------------------------------------
# PRIVATE HELPERS
# ---------------------------------------------------------------------------


def _group_parents_by_family(parents: list[Parent]) -> dict[str, list[Parent]]:
    grouped: dict[str, list[Parent]] = {}
    for p in parents:
        grouped.setdefault(p.family_id, []).append(p)
    return grouped


def _group_children_by_family(children: list[Child]) -> dict[str, list[Child]]:
    grouped: dict[str, list[Child]] = {}
    for c in children:
        grouped.setdefault(c.family_id, []).append(c)
    return grouped


def _extract_mother_father(parents: list[Parent]):
    mother = None
    father = None

    for p in parents:
        if p.parental_role == ParentalRole.MOTHER:
            mother = p
        elif p.parental_role == ParentalRole.FATHER:
            father = p

    return mother, father


def _build_single_family(family_id: str, mother: Parent, father: Parent, children: list[Child]) -> Family:
    return Family(id=family_id, mother=mother, father=father, children=children)
