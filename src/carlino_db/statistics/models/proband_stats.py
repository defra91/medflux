from dataclasses import dataclass
from typing import Dict
from .symptom_frequency import SymptomFrequency

@dataclass
class ProbandStats:
    """Statistiche sui probandi (figli affetti)."""
    total_probands: int

    symptom_frequencies: Dict[str, SymptomFrequency]

    avg_age_onset: float
    avg_age_diagnosis: float

    biological_treatment_count: int
    biological_treatment_percentage: float