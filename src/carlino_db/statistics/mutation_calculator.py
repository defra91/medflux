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

            if mut is None:
                continue


            try:
                # considera solo mutazioni eterozigoti (singola variante)
                if any(sep in mut for sep in ["+", "/", ","]):
                    continue
            except Exception as e:
                print(f"Error processing mutation '{mut}': {e}")
                continue

            mutations.append(mut)

    # nessun genitore eterozigote → ritorna dizionario vuoto
    if not mutations:
        return {}

    total = len(mutations)
    counts = Counter(mutations)

    # frequenza relativa
    return {mutation: count / total for mutation, count in counts.items()}


def mutation_symptom_association_counts(families: list[Family], mutation: str) -> dict[str, dict[str, int]]:
    """
    Count, for each symptom, how many probands and parents with the specified mutation present it.
    The result is suitable for a grouped bar chart.
    """

    comparable_symptoms = [
        "abdominal_pain",
        "chest_pain",
        "osteoarticular_pain",
        "headache",
        "asthenia",
        "has_aphthosis",
        "has_tonsillitis",
    ]

    counts = {symptom: {"child": 0, "parent": 0} for symptom in comparable_symptoms}

    for family in families:
        if not family.children:
            continue

        matching_children = [child for child in family.children if child.mutation == mutation]
        if not matching_children:
            continue

        child = matching_children[0]
        parent = next((p for p in family.parents() if p.mutation == mutation), None)
        if parent is None:
            continue

        for symptom in comparable_symptoms:
            if getattr(child, symptom, False):
                counts[symptom]["child"] += 1
            if getattr(parent, symptom, False):
                counts[symptom]["parent"] += 1

    return counts
