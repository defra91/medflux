from collections import Counter

from ..domain.episode_duration import EpisodeDuration
from ..domain.family import Family
from ..domain.parent import Parent


def pathogenic_mutations() -> set[str]:
    return {"M694V", "M680I", "V726A", "M694I", "A744S", "E148Q", "R761H", "L695A", "A289V", "M528V", "K695R"}


def satisfies_eurofever(parent: Parent) -> bool:
    # Mutazioni MEFV patogenetiche secondo PRINTO/Eurofever

    bad_fever = parent.recurrent_fever and (
        parent.episode_duration == EpisodeDuration.BETWEEN_12_AND_72H
        or parent.episode_duration == EpisodeDuration.MORE_THAN_72H
    )

    # Criteri clinici FMF mappati sulla tua classe Parent
    clinical_criteria = [bad_fever, parent.chest_pain, parent.abdominal_pain, parent.osteoarticular_pain]

    # Conta quanti criteri clinici sono presenti
    num_clinical = sum(1 for c in clinical_criteria if c)

    # Regola Eurofever/PRINTO
    has_pathogenic_mut = parent.mutation in pathogenic_mutations()

    return has_pathogenic_mut and num_clinical >= 2


def extract_eurofever_mutations_frequency(families: list[Family]) -> dict[str, float]:
    # Conta le mutazioni dei genitori che soddisfano i criteri
    mutations = []

    for family in families:
        for parent in family.parents():
            if parent.mutation and satisfies_eurofever(parent):
                mutations.append(parent.mutation)

    # Se non ci sono genitori con mutazione, evita divisioni per zero
    if not mutations:
        return {}

    total = len(mutations)
    counts = Counter(mutations)

    # Frequenza = count / totale
    return {mutation: count / total for mutation, count in counts.items()}
