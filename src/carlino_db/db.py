# src/db.py

from pathlib import Path

import pandas as pd

from .models.family_record import FamilyRecord
from .models.patient_record import PatientRecord
from .normalization import normalize_cell_value


def load_family_records(db_path: Path) -> list[FamilyRecord]:
    """
    Load the first sheet of the Excel file and return a list of FamilyRecord instances.
    """

    df = pd.read_excel(db_path, sheet_name=0)

    df.columns = [
        "family_id",
        "padre_madre",
        "mutazione",
        "febbre_ricorrente",
        "t_max",
        "durata",
        "dol_addominale",
        "dol_toracico",
        "cefalea",
        "dol_osteoarticolari",
        "aftosi_con_febbre",
        "aftosi_senza_febbre",
        "tonsillite_eritematosa",
        "tonsillite_essudativa",
        "man_cutanee",
        "astenia",
        "irc",
        "febbre_eta_adulta",
        "amiloidosi_famiglia",
        "esordio_lt_18",
        "esordio_gt_18",
        "episodi_anno",
        "tonsillectomia",
        "appendicectomia",
        "miglioramento_eta_adulta",
        "fam_irc",
        "consanguineita",
    ]

    records = []
    for _, row in df.iterrows():
        raw = row.to_dict()
        data = {k: normalize_cell_value(v) for k, v in raw.items()}
        records.append(FamilyRecord(**data))

    return records


def load_patient_records(db_path: Path) -> list[PatientRecord]:
    """
    Load the second sheet of the Excel file and return a list of PatientRecord instances.
    """

    df = pd.read_excel(db_path, sheet_name=1)

    df.columns = [
        "centre_id",
        "family_id",
        "id_eurofever",
        "sesso",
        "country",
        "eta_esordio",
        "eta_diagnosi",
        "genitori_consanguinei",
        "familiarita",
        "genetica",
        "febbre",
        "tc_max",
        "durata_episodi",
        "episodi_anno",
        "trigger_febbre",
        "dol_add",
        "dia",
        "stip",
        "vom",
        "chir_add",
        "dol_toracico",
        "pericardite",
        "pleurite",
        "artralgia",
        "artrite",
        "mialgia",
        "dolore_osseo",
        "erisipela_like",
        "mucocutanee",
        "altro",
        "altro_2",  # <--- la colonna vuota!
        "terapia",
        "dosaggio_mg_die",
        "risp_alla_tx",
        "eff_collaterali",
        "terapia_biologica",
        "amiloidosi",
        "malattie_concomitanti",
    ]

    records: list[PatientRecord] = []

    for _, row in df.iterrows():
        raw = row.to_dict()
        normalized = {k: normalize_cell_value(v) for k, v in raw.items()}
        record = PatientRecord(**normalized)
        records.append(record)

    return records
