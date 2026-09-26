from dataclasses import dataclass
from typing import List

@dataclass
class ConcordanceEntry:
    """
    Concordanza fenotipica genitore figlio per una singola famiglia.
    """
    family_id: str
    mutation: str

    shared_symptoms: List[str]
    discordant_symptoms: List[str]

    concordance_score: float  # es: similarità Hamming o Jaccard