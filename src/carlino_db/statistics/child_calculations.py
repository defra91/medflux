from ..domain.abdominal_surgery import AbdominalSurgery
from ..domain.amyloidosis import Amyloidosis
from ..domain.child import Child
from ..domain.episode_duration import EpisodeDuration
from ..domain.fever_trigger import FeverTrigger
from ..domain.mucocutaneous import Mucocutaneous
from ..domain.temperature_category import TemperatureCategory


def extract_child_symptoms(child: Child) -> list[str]:
    symptoms = []

    # Fever-related
    if child.fever is True:
        symptoms.append("fever")

    if child.temperature_category and child.temperature_category != TemperatureCategory.NOT_PRESENT:
        symptoms.append(f"temperature_{child.temperature_category.name.lower()}")

    if child.episode_duration and child.episode_duration != EpisodeDuration.UNKNOWN:
        symptoms.append(f"episode_duration_{child.episode_duration.name.lower()}")

    if child.fever_trigger and child.fever_trigger != FeverTrigger.UNKNOWN and child.fever_trigger != FeverTrigger.NO:
        symptoms.append(f"fever_trigger_{child.fever_trigger.name.lower()}")

    # Abdominal
    if child.abdominal_pain:
        symptoms.append("abdominal_pain")
    if child.diarrhea:
        symptoms.append("diarrhea")
    if child.constipation:
        symptoms.append("constipation")
    if child.vomiting:
        symptoms.append("vomiting")

    if child.abdominal_surgery and child.abdominal_surgery != AbdominalSurgery.UNKNOWN:
        symptoms.append("abdominal_surgery")

    # Chest
    if child.chest_pain:
        symptoms.append("chest_pain")
    if child.pericarditis:
        symptoms.append("pericarditis")
    if child.pleuritis:
        symptoms.append("pleuritis")

    # Musculoskeletal
    if child.arthralgia:
        symptoms.append("arthralgia")
    if child.arthritis:
        symptoms.append("arthritis")
    if child.myalgia:
        symptoms.append("myalgia")
    if child.bone_pain:
        symptoms.append("bone_pain")

    # Skin / mucosa
    if child.erysipelas_like:
        symptoms.append("erysipelas_like")

    if (
        child.mucocutaneous
        and child.mucocutaneous != Mucocutaneous.NONE
        and child.mucocutaneous != Mucocutaneous.UNKNOWN
    ):
        symptoms.append(f"mucocutaneous_{child.mucocutaneous.name.lower()}")

    if child.other_manifestations and child.other_manifestations.strip().upper() != "NO":
        symptoms.append(child.other_manifestations)

    # Additional clinical indicators
    if child.amyloidosis and child.amyloidosis != Amyloidosis.UNKNOWN and child.amyloidosis != Amyloidosis.NO:
        symptoms.append("amyloidosis")

    if child.concomitant_diseases and child.concomitant_diseases.strip().upper() != "NO":
        symptoms.append(child.concomitant_diseases)

    return symptoms
