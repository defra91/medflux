from collections import Counter

from ..domain.family import Family
from ..domain.parent import Parent


def satisfies_eurofever(parent: Parent) -> bool:
    # Mutazioni MEFV patogenetiche secondo PRINTO/Eurofever
    pathogenic_mutations = {
        "M694V", "M680I", "V726A", "M694I", "A744S", "E148Q"
    }

    # Criteri clinici FMF mappati sulla tua classe Parent
    clinical_criteria = [
        parent.recurrent_fever,
        parent.abdominal_pain,
        parent.chest_pain,
        parent.osteoarticular_pain,
        parent.cutaneous_manifestations,
        parent.erythematous_tonsillitis,
        parent.exudative_tonsillitis,
    ]

    # Conta quanti criteri clinici sono presenti
    num_clinical = sum(1 for c in clinical_criteria if c)

    # Regola Eurofever/PRINTO
    has_pathogenic_mut = parent.mutation in pathogenic_mutations

    return (num_clinical >= 1 and has_pathogenic_mut) or (num_clinical >= 2)


def extract_eurofever_mutations_frequency(families: list[Family]) -> dict[str, float]:
    # Conta le mutazioni dei genitori che soddisfano i criteri
    mutations = []

    for family in families:
        for parent in family.parents():
            if parent.mutation:          # ignora mutazioni vuote
                mutations.append(parent.mutation)

    # Se non ci sono genitori con mutazione, evita divisioni per zero
    if not mutations:
        return {}

    total = len(mutations)
    counts = Counter(mutations)

    # Frequenza = count / totale
    return {mutation: count / total for mutation, count in counts.items()}
