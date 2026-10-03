from collections import Counter, defaultdict

from ..domain.episode_duration import EpisodeDuration
from ..domain.parent import Parent
from ..domain.temperature_category import TemperatureCategory


def extract_parent_symptoms(parent: Parent) -> list[str]:
    symptoms = []

    # Fever-related
    if parent.recurrent_fever:
        symptoms.append("fever")

    if parent.temperature_category and parent.temperature_category != TemperatureCategory.NOT_PRESENT:
        symptoms.append(f"temperature_{parent.temperature_category.name.lower()}")

    if parent.episode_duration and parent.episode_duration != EpisodeDuration.UNKNOWN:
        symptoms.append(f"episode_duration_{parent.episode_duration.name.lower()}")

    # Abdominal
    if parent.abdominal_pain:
        symptoms.append("abdominal_pain")

    # Chest
    if parent.chest_pain:
        symptoms.append("chest_pain")

    # Headache
    if parent.headache:
        symptoms.append("headache")

    # Musculoskeletal
    if parent.osteoarticular_pain:
        symptoms.append("osteoarticular_pain")

    # Aphthosis
    if parent.aphthosis_with_fever:
        symptoms.append("aphthosis_with_fever")

    if parent.aphthosis_without_fever:
        symptoms.append("aphthosis_without_fever")

    # Tonsillitis
    if parent.erythematous_tonsillitis:
        symptoms.append("erythematous_tonsillitis")

    if parent.exudative_tonsillitis:
        symptoms.append("exudative_tonsillitis")

    # Skin
    if parent.cutaneous_manifestations:
        symptoms.append("cutaneous_manifestations")

    # Asthenia
    if parent.asthenia:
        symptoms.append("asthenia")

    # Respiratory
    if parent.respiratory_infections_chronic:
        symptoms.append("respiratory_infections_chronic")

    # Adult fever
    if parent.fever_in_adulthood:
        symptoms.append("fever_in_adulthood")

    # Procedures
    if parent.tonsillectomy:
        symptoms.append("tonsillectomy")

    if parent.appendicectomy:
        symptoms.append("appendicectomy")

    return symptoms



def compute_phenotype_distribution_by_mutation(parents: list[Parent]) -> dict[str, dict]:
    grouped: dict[str, list[Parent]] = defaultdict(list)

    # Raggruppa i genitori per mutazione
    for parent in parents:
        if parent.mutation:
            grouped[parent.mutation].append(parent)

    result: dict[str, dict] = {}

    for mutation, group in grouped.items():
        total = len(group)

        # Estrai tutti i sintomi dei genitori portatori della mutazione
        all_symptoms = []
        for parent in group:
            all_symptoms.extend(extract_parent_symptoms(parent))

        counter = Counter(all_symptoms)

        symptoms_stats = {
            symptom: {
                "count": count,
                "percentage": (count / total) * 100 if total > 0 else 0
            }
            for symptom, count in counter.items()
        }

        result[mutation] = {
            "total": total,
            "symptoms": symptoms_stats
        }

    return result
