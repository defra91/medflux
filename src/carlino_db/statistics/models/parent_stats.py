from dataclasses import dataclass
from itertools import count
from typing import Dict, List, Optional
from .symptom_frequency import SymptomFrequency
from .mutation_frequency import MutationFrequency
from .phenotype_profile import PhenotypeProfile
from .age_group_count import AgeGroupCount

@dataclass
class ParentStats:
    """Statistiche sui genitori."""
    total_parents: int

    consanguinity_present: bool
    consanguinity_rate: float

    symptomatic_parents_count: int
    symptomatic_parents_percentage: float

    symptom_frequencies: Dict[str, SymptomFrequency]
    mutation_frequencies: Dict[str, MutationFrequency]

    avg_age_onset: Optional[float]
    age_onset_groups: List[AgeGroupCount]

    phenotype_profiles: Dict[str, PhenotypeProfile]  # parent_id -> profile