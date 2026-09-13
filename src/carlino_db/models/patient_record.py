from pydantic import BaseModel
from typing import Optional

class PatientRecord(BaseModel):
    centre_id: str
    family_id: str
    id_eurofever: Optional[str]
    sesso: Optional[str]
    country: Optional[str]

    eta_esordio: Optional[str]
    eta_diagnosi: Optional[str]

    genitori_consanguinei: Optional[str]
    familiarita: Optional[str]

    genetica: Optional[str]

    febbre: Optional[str]
    tc_max: Optional[str]
    durata_episodi: Optional[str]
    episodi_anno: Optional[str]

    trigger_febbre: Optional[str]

    dol_add: Optional[str]
    dia: Optional[str]
    stip: Optional[str]
    vom: Optional[str]
    chir_add: Optional[str]

    dol_toracico: Optional[str]
    pericardite: Optional[str]
    pleurite: Optional[str]

    artralgia: Optional[str]
    artrite: Optional[str]
    mialgia: Optional[str]
    dolore_osseo: Optional[str]

    erisipela_like: Optional[str]
    mucocutanee: Optional[str]
    altro: Optional[str]

    terapia: Optional[str]
    dosaggio_mg_die: Optional[str]
    risp_alla_tx: Optional[str]
    eff_collaterali: Optional[str]

    terapia_biologica: Optional[str]
    amiloidosi: Optional[str]
    malattie_concomitanti: Optional[str]
