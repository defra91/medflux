from dataclasses import dataclass

from .abdominal_surgery import AbdominalSurgery
from .amyloidosis import Amyloidosis
from .collateral_effects import CollateralEffects
from .country import Country
from .episode_duration import EpisodeDuration
from .fever_trigger import FeverTrigger
from .gender import Gender
from .mucocutaneous import Mucocutaneous
from .mutation import Mutation
from .optional_bool import OptionalBool
from .temperature_category import TemperatureCategory
from .therapy_response import TherapyResponse


@dataclass
class Child:
    """
    Represents a child in the domain model.
    """

    centre_id: str
    family_id: str
    eurofever_id: str
    gender: Gender
    country: Country

    onset_age_years: int
    diagnosis_age_years: int

    parents_consanguineous: OptionalBool
    familiality: OptionalBool

    mutation: Mutation

    fever: OptionalBool
    temperature_category: TemperatureCategory
    episode_duration: EpisodeDuration
    episodes_per_year: int
    fever_trigger: FeverTrigger

    abdominal_pain: bool
    diarrhea: bool
    constipation: bool
    vomiting: bool
    abdominal_surgery: AbdominalSurgery

    chest_pain: bool
    pericarditis: bool
    pleuritis: bool

    arthralgia: bool
    arthritis: bool
    myalgia: bool
    bone_pain: bool

    erysipelas_like: bool
    mucocutaneous: Mucocutaneous
    other_manifestations: str

    therapy: OptionalBool
    dosage_mg_day: float
    therapy_response: TherapyResponse
    side_effects: CollateralEffects
    biological_therapy: bool

    amyloidosis: Amyloidosis
    concomitant_diseases: str
