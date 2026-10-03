from dataclasses import dataclass

from .concordance_entry import ConcordanceEntry


@dataclass
class ConcordanceStats:
    """Statistiche di concordanza genitore–figlio."""

    per_family: list[ConcordanceEntry]
    avg_concordance: float
    concordance_by_mutation: dict[str, float]
