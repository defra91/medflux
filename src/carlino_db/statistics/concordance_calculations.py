from .child_calculations import extract_child_symptoms
from .parent_calculations import extract_parent_symptoms

# ============================================================
# 3. Concordance score (Jaccard index)
# ============================================================

def concordance(parent_symptoms: list[str], child_symptoms: list[str]) -> float:
    set_parent = set(parent_symptoms)
    set_child = set(child_symptoms)

    intersection = len(set_parent & set_child)
    union = len(set_parent | set_child)

    return intersection / union if union > 0 else 0.0


def compute_concordance_by_mutation(families) -> list[dict]:
    """
    Compute concordance between parent and child who share the same mutation.
    Returns a flat list of entries, each containing mutation as a field.
    """

    result: list[dict] = []

    for family in families:

        # Identify proband (first child)
        proband = None
        for child in family.children:
            proband = child
            break

        if not proband:
            continue

        mutation = proband.mutation

        # Identify parent with same mutation
        parent = None
        if family.mother and family.mother.mutation == mutation:
            parent = family.mother
        elif family.father and family.father.mutation == mutation:
            parent = family.father

        # Skip families where no parent has the same mutation
        if not parent:
            continue

        # Extract symptoms
        parent_symptoms = extract_parent_symptoms(parent)
        child_symptoms = extract_child_symptoms(proband)

        # Compute concordance
        score = concordance(parent_symptoms, child_symptoms)

        entry = {
            "family_id": family.id,
            "mutation": mutation,
            "parent_role": parent.parental_role.name,
            "parent_symptoms": parent_symptoms,
            "child_symptoms": child_symptoms,
            "shared_symptoms": list(set(parent_symptoms) & set(child_symptoms)),
            "discordant_symptoms": list(set(parent_symptoms) ^ set(child_symptoms)),
            "concordance_score": score,
        }

        result.append(entry)

    return result
