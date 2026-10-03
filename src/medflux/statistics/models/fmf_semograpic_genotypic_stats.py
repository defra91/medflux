from dataclasses import dataclass


@dataclass
class FMFDemographicGenotypicStats:
    # --- Sesso ---
    count_m: int
    count_f: int
    percentage_m: float
    percentage_f: float

    # --- Genotipo ---
    count_heterozygous_simple: int
    count_heterozygous_compound: int
    count_homozygous: int

    percentage_heterozygous_simple: float
    percentage_heterozygous_compound: float
    percentage_homozygous: float

    # Provenienza geografica
    count_origin_local: int
    count_origin_foreign: int
    percentage_origin_local: float
    percentage_origin_foreign: float

    average_onset_age: float
    average_difference_diagnosis_onset: float
    count_biologic_therapy: int
    percentage_biologic_theraphy: float
