from dataclasses import dataclass
from typing import Dict

from .mutation_group_stats import MutationGroupStats
from .family_stats import FamilyStats
from .proband_stats import ProbandStats
from .parent_stats import ParentStats
from .concordance_stats import ConcordanceStats


@dataclass
class Statistics:
    """Contenitore completo di tutte le statistiche del progetto."""
    families: FamilyStats
    probands: ProbandStats
    parents: ParentStats
    concordance: ConcordanceStats
    mutation_groups: Dict[str, MutationGroupStats]