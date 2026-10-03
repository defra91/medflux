# src/medflux/models/family_record.py


from pydantic import BaseModel


class FamilyRecord(BaseModel):
    family_id: str
    padre_madre: str | None
    mutazione: str | None

    febbre_ricorrente: str | None
    t_max: str | None
    durata: str | None

    dol_addominale: str | None
    dol_toracico: str | None
    cefalea: str | None
    dol_osteoarticolari: str | None

    aftosi_con_febbre: str | None
    aftosi_senza_febbre: str | None

    tonsillite_eritematosa: str | None
    tonsillite_essudativa: str | None

    man_cutanee: str | None
    astenia: str | None
    irc: str | None

    febbre_eta_adulta: str | None
    amiloidosi_famiglia: str | None

    esordio_lt_18: str | None
    esordio_gt_18: str | None

    episodi_anno: str | None
    tonsillectomia: str | None
    appendicectomia: str | None

    miglioramento_eta_adulta: str | None
    fam_irc: str | None
    consanguineita: str | None
