import re

from ..domain.child import Child
from ..models.patient_record import PatientRecord
from .base_mappers import (
    map_abdominal_surgery,
    map_amyloidosis,
    map_boolean,
    map_collateral_effects,
    map_country,
    map_episode_duration,
    map_family_id,
    map_fever_trigger,
    map_float,
    map_gender,
    map_int,
    map_mucocutaneous,
    map_mutation,
    map_optional_bool,
    map_str,
    map_temperature_category,
    map_therapy_response,
)


def map_child(patient_record: PatientRecord) -> Child:
    """
    Map a PatientRecord to a Child domain model.
    """

    altro = patient_record.altro or ""

    return Child(
        # Identifiers
        centre_id=map_str(patient_record.centre_id),
        family_id=map_family_id(patient_record.family_id),
        eurofever_id=map_str(patient_record.id_eurofever),
        # Demographics
        gender=map_gender(patient_record.sesso),
        country=map_country(patient_record.country),
        # Ages
        onset_age_years=map_int(patient_record.eta_esordio),
        diagnosis_age_years=map_int(patient_record.eta_diagnosi),
        # Family history
        parents_consanguineous=map_optional_bool(patient_record.genitori_consanguinei),
        familiality=map_optional_bool(patient_record.familiarita),
        # Genetics
        mutation=patient_record.genetica.upper(),
        # Fever & episodes
        fever=map_optional_bool(patient_record.febbre),
        temperature_category=map_temperature_category(patient_record.tc_max),
        episode_duration=map_episode_duration(patient_record.durata_episodi),
        episodes_per_year=map_int(patient_record.episodi_anno),
        fever_trigger=map_fever_trigger(patient_record.trigger_febbre),
        # Abdominal
        abdominal_pain=map_boolean(patient_record.dol_add),
        diarrhea=map_boolean(patient_record.dia),
        constipation=map_boolean(patient_record.stip),
        vomiting=map_boolean(patient_record.vom),
        abdominal_surgery=map_abdominal_surgery(patient_record.chir_add),
        # Chest
        chest_pain=map_boolean(patient_record.dol_toracico),
        pericarditis=map_boolean(patient_record.pericardite),
        pleuritis=map_boolean(patient_record.pleurite),
        # Musculoskeletal
        arthralgia=map_boolean(patient_record.artralgia),
        arthritis=map_boolean(patient_record.artrite),
        myalgia=map_boolean(patient_record.mialgia),
        bone_pain=map_boolean(patient_record.dolore_osseo),
        # Skin / mucosa
        erysipelas_like=map_boolean(patient_record.erisipela_like),
        mucocutaneous=map_mucocutaneous(patient_record.mucocutanee),
        other_manifestations=map_str(patient_record.altro),
        # Therapy
        therapy=map_optional_bool(patient_record.terapia),
        dosage_mg_day=map_float(patient_record.dosaggio_mg_die),
        therapy_response=map_therapy_response(patient_record.risp_alla_tx),
        side_effects=map_collateral_effects(patient_record.eff_collaterali),
        biological_therapy=map_boolean(patient_record.terapia_biologica),
        # Complications / comorbidities
        amyloidosis=map_amyloidosis(patient_record.amiloidosi),
        concomitant_diseases=map_str(patient_record.malattie_concomitanti),

        headache=bool(
            re.search(r"\bcefalea\b", altro, flags=re.IGNORECASE)
        ),

        asthenia=bool(
            re.search(r"\bastenia\b", altro, flags=re.IGNORECASE)
        ),
    )
