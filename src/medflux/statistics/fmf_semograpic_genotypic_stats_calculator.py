from collections import Counter

from ..domain.country import Country
from ..domain.family import Family
from ..domain.gender import Gender
from ..domain.optional_bool import OptionalBool
from .models.fmf_semograpic_genotypic_stats import FMFDemographicGenotypicStats


def is_simple_heterozygous(patient) -> bool:
    mut = getattr(patient, "mutation", None)
    if not mut:
        return False

    # nessun separatore → singola mutazione
    return not any(sep in mut for sep in ["+", "/", ","])


def is_compound_heterozygous(patient) -> bool:
    mut = getattr(patient, "mutation", None)
    if not mut:
        return False

    # separatori → più mutazioni
    if not any(sep in mut for sep in ["+", "/", ","]):
        return False

    # split su tutti i separatori
    import re

    parts = re.split(r"[+/,\s]+", mut)

    # almeno due mutazioni diverse
    return len(parts) == 2 and parts[0] != parts[1]


def genotype_category(patient) -> str:
    if is_homozygous(patient):
        return "homozygous"
    if is_compound_heterozygous(patient):
        return "compound"
    if is_simple_heterozygous(patient):
        return "simple"
    return "unknown"


def is_homozygous(patient) -> bool:
    mut = getattr(patient, "mutation", None)
    if not mut:
        return False

    import re

    parts = re.split(r"[+/,\s]+", mut)

    # due copie identiche
    return len(parts) == 2 and parts[0] == parts[1]


def is_origin_local(patient) -> bool:
    origin = getattr(patient, "country", None)
    if not origin:
        return False

    return origin == Country.ITALY


def is_origin_foreign(patient) -> bool:
    origin = getattr(patient, "country", None)
    if not origin:
        return False

    return origin == Country.ABROAD


def calculate_fmf_demographic_genotypic_stats(families: list[Family]) -> FMFDemographicGenotypicStats:
    # --- 1. Estrai TUTTI i children FMF ---
    fmf_children = []

    for family in families:
        for child in family.children:
            fmf_children.append(child)

    # Nessun paziente FMF → ritorna oggetto vuoto
    if not fmf_children:
        return FMFDemographicGenotypicStats(
            count_m=0,
            count_f=0,
            percentage_m=0.0,
            percentage_f=0.0,
            count_heterozygous_simple=0,
            count_heterozygous_compound=0,
            count_homozygous=0,
            percentage_heterozygous_simple=0.0,
            percentage_heterozygous_compound=0.0,
            percentage_homozygous=0.0,
            count_origin_local=0,
            count_origin_foreign=0,
            percentage_origin_local=0.0,
            percentage_origin_foreign=0.0,
        )

    total = len(fmf_children)

    # --- 2. Calcolo sesso ---
    sex_counts = Counter(child.gender for child in fmf_children)

    count_m = sex_counts.get(Gender.MALE, 0)
    count_f = sex_counts.get(Gender.FEMALE, 0)

    percentage_m = round(count_m / total * 100, 2)
    percentage_f = round(count_f / total * 100, 2)

    # --- 3. Calcolo genotipo ---
    count_simple = sum(1 for c in fmf_children if is_simple_heterozygous(c))
    count_compound = sum(1 for c in fmf_children if is_compound_heterozygous(c))
    count_homo = sum(1 for c in fmf_children if is_homozygous(c))

    percentage_simple = round(count_simple / total * 100, 2)
    percentage_compound = round(count_compound / total * 100, 2)
    percentage_homo = round(count_homo / total * 100, 2)

    # --- 4. Calcolo provenienza geografica ---
    count_origin_local = sum(1 for c in fmf_children if is_origin_local(c))
    count_origin_foreign = sum(1 for c in fmf_children if is_origin_foreign(c))

    percentage_origin_local = round(count_origin_local / total * 100, 2)
    percentage_origin_foreign = round(count_origin_foreign / total * 100, 2)

    average_onset_age = (
        round(sum(c.onset_age_years for c in fmf_children if c.onset_age_years is not None) / total, 2)
        if total > 0
        else 0.0
    )

    differences = [
        abs(c.diagnosis_age_years - c.onset_age_years)
        for c in fmf_children
        if c.onset_age_years is not None and c.diagnosis_age_years is not None
    ]

    average_difference_diagnosis_onset = round(sum(differences) / len(differences), 2) if len(differences) > 0 else 0.0

    with_therapy = sum(1 for c in fmf_children if c.therapy == OptionalBool.TRUE)
    with_biologic_therapy = sum(1 for c in fmf_children if c.therapy == OptionalBool.TRUE and c.biological_therapy)

    percentage_biologic_theraphy = round(with_biologic_therapy / with_therapy * 100, 2) if with_therapy > 0 else 0.0

    # --- 5. Costruzione oggetto finale ---
    return FMFDemographicGenotypicStats(
        count_m=count_m,
        count_f=count_f,
        percentage_m=percentage_m,
        percentage_f=percentage_f,
        count_heterozygous_simple=count_simple,
        count_heterozygous_compound=count_compound,
        count_homozygous=count_homo,
        percentage_heterozygous_simple=percentage_simple,
        percentage_heterozygous_compound=percentage_compound,
        percentage_homozygous=percentage_homo,
        count_origin_local=count_origin_local,
        count_origin_foreign=count_origin_foreign,
        percentage_origin_local=percentage_origin_local,
        percentage_origin_foreign=percentage_origin_foreign,
        average_onset_age=average_onset_age,
        average_difference_diagnosis_onset=average_difference_diagnosis_onset,
        count_biologic_therapy=with_biologic_therapy,
        percentage_biologic_theraphy=percentage_biologic_theraphy,
    )
