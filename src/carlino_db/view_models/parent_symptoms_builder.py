from ..domain.episode_duration import EpisodeDuration
from ..domain.parent import Parent
from ..domain.temperature_category import TemperatureCategory


def build_parent_symptoms(parent: Parent) -> list[str]:
    symptoms = []

    if (parent.recurrent_fever):
        symptoms.append("Recurrent fever")

    if parent.temperature_category and parent.temperature_category != TemperatureCategory.NOT_PRESENT:
        symptoms.append("Temperature: " + parent.temperature_category.name.replace("_", " ").title())

    if parent.episode_duration and parent.episode_duration != EpisodeDuration.UNKNOWN:
        symptoms.append("Episode duration: " + parent.episode_duration.name.replace("_", " ").title())

    if parent.abdominal_pain:
        symptoms.append("Abdominal pain")

    if parent.chest_pain:
        symptoms.append("Chest pain")

    if parent.headache:
        symptoms.append("Headache")

    if parent.osteoarticular_pain:
        symptoms.append("Osteoarticular pain")

    if parent.aphthosis_with_fever:
        symptoms.append("Aphthosis with fever")

    if parent.aphthosis_without_fever:
        symptoms.append("Aphthosis without fever")

    if parent.erythematous_tonsillitis:
        symptoms.append("Erythematous tonsillitis")

    if parent.exudative_tonsillitis:
        symptoms.append("Exudative tonsillitis")

    if parent.cutaneous_manifestations:
        symptoms.append("Cutaneous manifestations")

    if parent.asthenia:
        symptoms.append("Asthenia")

    if parent.respiratory_infections_chronic:
        symptoms.append("Chronic respiratory infections")

    if parent.fever_in_adulthood:
        symptoms.append("Fever in adulthood")

    if parent.family_amyloidosis:
        symptoms.append("Family amyloidosis")

    if parent.onset_before_18:
        symptoms.append("Onset before 18")

    if parent.onset_after_18:
        symptoms.append("Onset after 18")

    if parent.tonsillectomy:
        symptoms.append("Tonsillectomy")

    if parent.appendicectomy:
        symptoms.append("Appendicectomy")

    if parent.family_respiratory_infections_chronic:
        symptoms.append("Family chronic respiratory infections")

    return symptoms
