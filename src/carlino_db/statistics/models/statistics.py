from dataclasses import dataclass

from .fmf_semograpic_genotypic_stats import FMFDemographicGenotypicStats
from .statistics_chart import StatisticsChart


@dataclass
class Statistics:
    """Contenitore completo di tutte le statistiche del progetto."""

    proband_distribution: list[dict]
    parent_distribution: list[dict]

    phenotype_distribution_by_mutation: dict[str, dict]

    concordance_by_mutation: list[dict]

    charts: list[StatisticsChart]

    fmf_demographic_genotypic_stats: FMFDemographicGenotypicStats

    symptoms_pvalues: dict[str, float]

    adult_onset_improvement_pvalue: float

    parents_cnt_with_eurofever: int
