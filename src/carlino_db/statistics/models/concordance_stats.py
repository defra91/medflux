from dataclasses import dataclass
from .concordance_entry import ConcordanceEntry
from typing import List, Dict


@dataclass
class ConcordanceStats:
    """Statistiche di concordanza genitore–figlio."""
    per_family: List[ConcordanceEntry]
    avg_concordance: float
    concordance_by_mutation: Dict[str, float]