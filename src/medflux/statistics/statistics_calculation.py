from ..domain.family import Family
from .charts_calculator import calculate_charts
from .concordance_calculations import compute_concordance_by_mutation
from .eurofever_calculator import satisfies_eurofever
from .family_calculations import compute_frequency_distribution, extract_mutations
from .fmf_semograpic_genotypic_stats_calculator import calculate_fmf_demographic_genotypic_stats
from .models.statistics import Statistics
from .p_values import calculate_adult_onset_improvement_pvalue, calculate_symptom_pvalues
from .parent_calculations import compute_phenotype_distribution_by_mutation


def calculate_statistics(families: list[Family]) -> Statistics:
    """
    Calcola tutte le statistiche del progetto a partire dalla lista di famiglie.
    Restituisce un oggetto Statistics completamente popolato.
    """

    proband_mut, parent_mut = extract_mutations(families)
    proband_distribution = compute_frequency_distribution(proband_mut)
    parent_distribution = compute_frequency_distribution(parent_mut)

    phenotype_distribution_by_mutation = compute_phenotype_distribution_by_mutation(
        [parent for family in families for parent in family.parents()]
    )

    concordance_by_mutation = compute_concordance_by_mutation(families)

    charts = calculate_charts(families)

    symptom_keys = [
        "abdominal_pain",
        "chest_pain",
        "osteoarticular_pain",
        "headache",
        "asthenia",
        "has_aphthosis",
        "has_tonsillitis",
    ]
    symptoms_pvalues = calculate_symptom_pvalues(families, symptom_keys)

    return Statistics(
        proband_distribution=proband_distribution,
        parent_distribution=parent_distribution,
        phenotype_distribution_by_mutation=phenotype_distribution_by_mutation,
        concordance_by_mutation=concordance_by_mutation,
        charts=charts,
        fmf_demographic_genotypic_stats=calculate_fmf_demographic_genotypic_stats(families),
        symptoms_pvalues=symptoms_pvalues,
        adult_onset_improvement_pvalue=calculate_adult_onset_improvement_pvalue(families),
        parents_cnt_with_eurofever=sum(
            1 for family in families for parent in family.parents() if satisfies_eurofever(parent)
        ),
    )
