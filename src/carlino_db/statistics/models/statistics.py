from dataclasses import dataclass

from .concordance_stats import ConcordanceStats
from .family_stats import FamilyStats
from .mutation_group_stats import MutationGroupStats
from .parent_stats import ParentStats
from .proband_stats import ProbandStats


@dataclass
class Statistics:
    """Contenitore completo di tutte le statistiche del progetto."""

    families: FamilyStats
    probands: ProbandStats
    parents: ParentStats
    concordance: ConcordanceStats
    mutation_groups: dict[str, MutationGroupStats]
