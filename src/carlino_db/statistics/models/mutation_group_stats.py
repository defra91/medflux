from dataclasses import dataclass
from typing import Dict
from .symptom_frequency import SymptomFrequency

@dataclass
class MutationGroupStats:
    """
    Statistiche per gruppi di genitori portatori della stessa mutazione.
    """
    mutation: str
    count: int
    avg_similarity: float
    symptom_frequencies: Dict[str, SymptomFrequency]