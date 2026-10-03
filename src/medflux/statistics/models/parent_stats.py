from dataclasses import dataclass

from .age_group_count import AgeGroupCount
from .mutation_frequency import MutationFrequency
from .phenotype_profile import PhenotypeProfile
from .symptom_frequency import SymptomFrequency


@dataclass
class ParentStats:
    """Statistiche sui genitori."""

    total_parents: int

    consanguinity_present: bool
    consanguinity_rate: float

    symptomatic_parents_count: int
    symptomatic_parents_percentage: float

    symptom_frequencies: dict[str, SymptomFrequency]
    mutation_frequencies: dict[str, MutationFrequency]

    avg_age_onset: float | None
    age_onset_groups: list[AgeGroupCount]

    phenotype_profiles: dict[str, PhenotypeProfile]  # parent_id -> profile
