# src/carlino_db/domain/parent.py

from dataclasses import dataclass

from .episode_duration import EpisodeDuration
from .parental_role import ParentalRole
from .temperature_category import TemperatureCategory


@dataclass
class Parent:
    family_id: str
    parental_role: ParentalRole
    mutation: str

    consanguinity: bool

    # Comparable symptoms
    abdominal_pain: bool
    chest_pain: bool
    headache: bool
    asthenia: bool

    has_tonsillitis: bool

    recurrent_fever: bool
    temperature_category: TemperatureCategory
    episode_duration: EpisodeDuration
    osteoarticular_pain: bool

    aphthosis_with_fever: bool
    aphthosis_without_fever: bool
    has_aphthosis: bool

    erythematous_tonsillitis: bool
    exudative_tonsillitis: bool
    cutaneous_manifestations: bool
    respiratory_infections_chronic: bool
    fever_in_adulthood: bool
    family_amyloidosis: bool
    onset_before_18: bool
    onset_after_18: bool
    episodes_per_year: int
    tonsillectomy: bool
    appendicectomy: bool
    improvement_in_adulthood: bool
    family_respiratory_infections_chronic: bool
