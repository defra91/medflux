from dataclasses import dataclass


@dataclass
class MutationFrequency:
    """Frequenza di una mutazione MEFV."""

    mutation: str
    count: int
    percentage: float
