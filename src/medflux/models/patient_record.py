from pydantic import BaseModel


class PatientRecord(BaseModel):
    centre_id: str
    family_id: str
    id_eurofever: str | None
    sesso: str | None
    country: str | None

    eta_esordio: str | None
    eta_diagnosi: str | None

    genitori_consanguinei: str | None
    familiarita: str | None

    genetica: str | None

    febbre: str | None
    tc_max: str | None
    durata_episodi: str | None
    episodi_anno: str | None

    trigger_febbre: str | None

    dol_add: str | None
    dia: str | None
    stip: str | None
    vom: str | None
    chir_add: str | None

    dol_toracico: str | None
    pericardite: str | None
    pleurite: str | None

    artralgia: str | None
    artrite: str | None
    mialgia: str | None
    dolore_osseo: str | None

    erisipela_like: str | None
    mucocutanee: str | None
    altro: str | None

    terapia: str | None
    dosaggio_mg_die: str | None
    risp_alla_tx: str | None
    eff_collaterali: str | None

    terapia_biologica: str | None
    amiloidosi: str | None
    malattie_concomitanti: str | None
