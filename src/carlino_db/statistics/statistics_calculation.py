from ..domain.family import Family
from .charts_calculator import calculate_charts
from .concordance_calculations import compute_concordance_by_mutation
from .family_calculations import compute_frequency_distribution, extract_mutations
from .models.concordance_stats import ConcordanceStats
from .models.family_stats import FamilyStats
from .models.mutation_group_stats import MutationGroupStats
from .models.parent_stats import ParentStats
from .models.proband_stats import ProbandStats
from .models.statistics import Statistics
from .parent_calculations import compute_phenotype_distribution_by_mutation


def calculate_statistics(families: list[Family]) -> Statistics:
    """
    Calcola tutte le statistiche del progetto a partire dalla lista di famiglie.
    Restituisce un oggetto Statistics completamente popolato.
    """
    family_stats = calculate_family_stats(families)
    proband_stats = calculate_proband_stats(families)
    parent_stats = calculate_parent_stats(families)
    concordance_stats = calculate_concordance_stats(families)
    mutation_groups = calculate_mutation_group_stats(families)

    proband_mut, parent_mut = extract_mutations(families)
    proband_distribution = compute_frequency_distribution(proband_mut)
    parent_distribution = compute_frequency_distribution(parent_mut)

    phenotype_distribution_by_mutation = compute_phenotype_distribution_by_mutation(
        [parent for family in families for parent in family.parents()])

    concordance_by_mutation = compute_concordance_by_mutation(families)

    charts = calculate_charts(families)

    return Statistics(
        families=family_stats,
        probands=proband_stats,
        parents=parent_stats,
        concordance=concordance_stats,
        mutation_groups=mutation_groups,

        proband_distribution=proband_distribution,
        parent_distribution=parent_distribution,
        phenotype_distribution_by_mutation=phenotype_distribution_by_mutation,
        concordance_by_mutation=concordance_by_mutation,
        charts=charts,
    )


def calculate_family_stats(families: list[Family]) -> FamilyStats:
    """
    Calcola:
    - numero famiglie
    - numero totale figli
    - media figli per famiglia
    """
    # TODO: implementazione
    return FamilyStats(
        total_families=0,
        total_children=0,
        avg_children_per_family=0.0,
    )


def calculate_proband_stats(families: list[Family]) -> ProbandStats:
    """
    Calcola statistiche sui probandi:
    - frequenza sintomi
    - età media esordio
    - età media diagnosi
    - terapia biologica (assoluto + percentuale)
    """
    # TODO: implementazione
    return ProbandStats(
        total_probands=0,
        symptom_frequencies={},
        avg_age_onset=0.0,
        avg_age_diagnosis=0.0,
        biological_treatment_count=0,
        biological_treatment_percentage=0.0,
    )


def calculate_parent_stats(families: list[Family]) -> ParentStats:
    """
    Calcola statistiche sui genitori:
    - consanguineità
    - sintomi più frequenti
    - mutazioni MEFV
    - età di esordio
    - gruppi di età
    - profili fenotipici
    """
    # TODO: implementazione
    return ParentStats(
        total_parents=0,
        consanguinity_present=False,
        consanguinity_rate=0.0,
        symptomatic_parents_count=0,
        symptomatic_parents_percentage=0.0,
        symptom_frequencies={},
        mutation_frequencies={},
        avg_age_onset=None,
        age_onset_groups=[],
        phenotype_profiles={},
    )


def calculate_concordance_stats(families: list[Family]) -> ConcordanceStats:
    """
    Calcola la concordanza genitore–figlio:
    - sintomi condivisi
    - sintomi discordanti
    - concordanza per famiglia
    - concordanza media
    - concordanza per mutazione
    """
    # TODO: implementazione
    return ConcordanceStats(
        per_family=[],
        avg_concordance=0.0,
        concordance_by_mutation={},
    )


def calculate_mutation_group_stats(families: list[Family]) -> dict[str, MutationGroupStats]:
    """
    Calcola statistiche per gruppi di genitori portatori della stessa mutazione:
    - numero soggetti
    - similarità media
    - frequenza sintomi
    """
    # TODO: implementazione
    return {}
