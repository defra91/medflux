from collections import Counter

from ..domain.family import Family


def extract_heterozygous_mutation_frequency(families: list[Family]) -> dict[str, float]:
    mutations = []

    for family in families:
        for parent in family.parents():
            mut = parent.mutation

            # ignora mutazioni vuote o None
            if not mut:
                continue

            # considera solo mutazioni eterozigoti (singola variante)
            if any(sep in mut for sep in ["+", "/", ","]):
                continue

            mutations.append(mut)

    # nessun genitore eterozigote → ritorna dizionario vuoto
    if not mutations:
        return {}

    total = len(mutations)
    counts = Counter(mutations)

    # frequenza relativa
    return {mutation: count / total for mutation, count in counts.items()}
