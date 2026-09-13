# src/carlino_db/domain/parent.py

from dataclasses import dataclass
from .parental_role import ParentalRole
from .temperature_category import TemperatureCategory
from .episode_duration import EpisodeDuration

@dataclass
class Parent:

    family_id: str
    parental_role: ParentalRole
    mutation: str
    recurrent_fever: bool
    temperature_category: TemperatureCategory
    episode_duration: EpisodeDuration
    abdominal_pain: bool
    chest_pain: bool 
    headache: bool
    osteoarticular_pain: bool
    aphthosis_with_fever: bool
    aphthosis_without_fever: bool
    erythematous_tonsillitis: bool
    exudative_tonsillitis: bool
    cutaneous_manifestations: bool
    asthenia: bool
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
    consanguinity: bool