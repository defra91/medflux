from collections import Counter

from ..domain.family import Family


def extract_mutations(families: list[Family]) -> tuple[list[str], list[str]]:
    """
    Estrae le mutazioni dai probandi e dai genitori all'interno di una lista di famiglie.

    Restituisce una tupla contenente due liste:
    - la prima lista contiene le mutazioni dei probandi
    - la seconda lista contiene le mutazioni dei genitori
    """
    proband_mutations = []
    parent_mutations = []

    for family in families:
        for child in family.children:
            proband_mutations.append(child.mutation)

        if family.mother:
            parent_mutations.append(family.mother.mutation)

        if family.father:
            parent_mutations.append(family.father.mutation)

    return proband_mutations, parent_mutations


def compute_frequency_distribution(values: list[str]) -> list[dict]:
    total = len(values)
    counter = Counter(values)

    items = [
        {
            "mutation": mutation,
            "count": count,
            "percentage": (count / total) * 100 if total > 0 else 0
        }
        for mutation, count in counter.items()
    ]

    # Ordina per count decrescente
    items.sort(key=lambda x: x["percentage"], reverse=True)

    return items
