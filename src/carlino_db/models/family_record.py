# src/carlino_db/models/family_record.py

from pydantic import BaseModel
from typing import Optional

class FamilyRecord(BaseModel):
    family_id: str
    padre_madre: Optional[str]
    mutazione: Optional[str]

    febbre_ricorrente: Optional[str]
    t_max: Optional[str]
    durata: Optional[str]

    dol_addominale: Optional[str]
    dol_toracico: Optional[str]
    cefalea: Optional[str]
    dol_osteoarticolari: Optional[str]

    aftosi_con_febbre: Optional[str]
    aftosi_senza_febbre: Optional[str]

    tonsillite_eritematosa: Optional[str]
    tonsillite_essudativa: Optional[str]

    man_cutanee: Optional[str]
    astenia: Optional[str]
    irc: Optional[str]

    febbre_eta_adulta: Optional[str]
    amiloidosi_famiglia: Optional[str]

    esordio_lt_18: Optional[str]
    esordio_gt_18: Optional[str]

    episodi_anno: Optional[str]
    tonsillectomia: Optional[str]
    appendicectomia: Optional[str]

    miglioramento_eta_adulta: Optional[str]
    fam_irc: Optional[str]
    consanguineita: Optional[str]