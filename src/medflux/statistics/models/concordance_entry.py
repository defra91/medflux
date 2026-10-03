from dataclasses import dataclass


@dataclass
class ConcordanceEntry:
    """
    Concordanza fenotipica genitore figlio per una singola famiglia.
    """

    family_id: str
    mutation: str

    shared_symptoms: list[str]
    discordant_symptoms: list[str]

    concordance_score: float  # es: similarità Hamming o Jaccard
