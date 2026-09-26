from dataclasses import dataclass

@dataclass
class FamilyStats:
    """Statistiche familiari generali."""
    total_families: int
    total_children: int
    avg_children_per_family: float