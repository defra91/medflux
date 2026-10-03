from ..domain.abdominal_surgery import AbdominalSurgery
from ..domain.amyloidosis import Amyloidosis
from ..domain.child import Child
from ..domain.episode_duration import EpisodeDuration
from ..domain.fever_trigger import FeverTrigger
from ..domain.mucocutaneous import Mucocutaneous
from ..domain.temperature_category import TemperatureCategory


def build_child_symptoms(child: Child) -> list[str]:
    symptoms = []

    # Fever
    if child.fever is True:
        symptoms.append("Fever: ")
        if child.temperature_category and child.temperature_category != TemperatureCategory.NOT_PRESENT:
            symptoms.append(child.temperature_category.name.replace("_", " ").title())

    if child.episode_duration and child.episode_duration != EpisodeDuration.UNKNOWN:
        symptoms.append(f"Episode duration: {child.episode_duration.name.lower()}")

    if child.fever_trigger and child.fever_trigger != FeverTrigger.UNKNOWN and child.fever_trigger != FeverTrigger.NO:
        symptoms.append(f"Trigger: {child.fever_trigger.name.title()}")

    # Abdominal
    if child.abdominal_pain:
        symptoms.append("Abdominal pain")
    if child.diarrhea:
        symptoms.append("Diarrhea")
    if child.constipation:
        symptoms.append("Constipation")
    if child.vomiting:
        symptoms.append("Vomiting")
    if child.abdominal_surgery and child.abdominal_surgery != AbdominalSurgery.UNKNOWN:
        symptoms.append("Abdominal surgery")

    # Chest
    if child.chest_pain:
        symptoms.append("Chest pain")
    if child.pericarditis:
        symptoms.append("Pericarditis")
    if child.pleuritis:
        symptoms.append("Pleuritis")

    # Musculoskeletal
    if child.arthralgia:
        symptoms.append("Arthralgia")
    if child.arthritis:
        symptoms.append("Arthritis")
    if child.myalgia:
        symptoms.append("Myalgia")
    if child.bone_pain:
        symptoms.append("Bone pain")

    # Skin / mucosa
    if child.erysipelas_like:
        symptoms.append("Erysipelas-like")
    if child.mucocutaneous and child.mucocutaneous != Mucocutaneous.UNKNOWN:
        symptoms.append("Mucocutaneous involvement")

    if child.other_manifestations and child.other_manifestations.strip().upper() != "NO":
        symptoms.append(child.other_manifestations)

    # Additional clinical indicators
    if child.amyloidosis and child.amyloidosis != Amyloidosis.UNKNOWN and child.amyloidosis != Amyloidosis.NO:
        symptoms.append(f"Amyloidosis: {child.amyloidosis.name.replace('_', ' ').title()}")

    if child.concomitant_diseases and child.concomitant_diseases.strip().upper() != "NO":
        symptoms.append(child.concomitant_diseases)

    return symptoms
