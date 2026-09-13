from dataclasses import dataclass


@dataclass
class Statistics:
    total_families: int
    total_children: int

    avg_children_per_family: float

    # Concordance
    concordance_per_family: dict[str, float]
    avg_concordance: float

    # Similarity
    similarity_mother: dict[str, float]
    similarity_father: dict[str, float]
    avg_similarity_mother: float
    avg_similarity_father: float

    # Mutation groups
    mutation_stats: dict[str, dict]

    # Symptom frequencies
    symptom_frequencies: dict[str, float]

    # Other descriptive stats
    avg_episode_duration: float
    consanguinity_rate: float