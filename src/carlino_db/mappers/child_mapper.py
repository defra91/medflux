from ..domain.child import Child
from ..models.patient_record import PatientRecord
from .base_mappers import map_gender, map_country, map_str, map_int, map_boolean, map_mutation, map_fever_trigger, map_float, map_optional_bool, map_temperature_category


def map_child(patient_record: PatientRecord) -> Child:
    """
    Map a PatientRecord to a Child domain model.
    """

    return Child(
        # Identifiers
        centre_id=patient_record.centre_id,
        family_id=patient_record.family_id,
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
        mutation=map_mutation(patient_record.genetica),

        # Fever & episodes
        fever=map_optional_bool(patient_record.febbre),
        temperature_category=map_temperature_category(patient_record.tc_max),
        episode_duration_days=map_int(patient_record.durata_episodi),
        episodes_per_year=map_int(patient_record.episodi_anno),
        fever_trigger=map_fever_trigger(patient_record.trigger_febbre),

        # Abdominal
        abdominal_pain=map_boolean(patient_record.dol_add),
        diarrhea=map_boolean(patient_record.dia),
        constipation=map_boolean(patient_record.stip),
        vomiting=map_boolean(patient_record.vom),
        abdominal_surgery=map_boolean(patient_record.chir_add),

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
        mucocutaneous=map_boolean(patient_record.mucocutanee),
        other_manifestations=map_str(patient_record.altro),

        # Therapy
        therapy=map_boolean(patient_record.terapia),
        dosage_mg_day=map_float(patient_record.dosaggio_mg_die),
        therapy_response=map_boolean(patient_record.risp_alla_tx),
        side_effects=map_boolean(patient_record.eff_collaterali),
        biological_therapy=map_boolean(patient_record.terapia_biologica),

        # Complications / comorbidities
        amyloidosis=map_boolean(patient_record.amiloidosi),
        concomitant_diseases=map_str(patient_record.malattie_concomitanti),
    )
