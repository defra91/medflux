from ..domain.parent import Parent
from ..models.family_record import FamilyRecord
from ..domain.parental_role import ParentalRole
from .base_mappers import map_boolean, map_temperature_category, map_episode_duration, map_int

def parse_parental_role(raw: str | None) -> ParentalRole:
    if raw is None:
        return ParentalRole.UNKNOWN

    s = raw.strip().upper()

    if s in ("1", "1.0", "PADRE", "FATHER", "P"):
        return ParentalRole.FATHER

    if s in ("2", "2.0", "MADRE", "MOTHER", "M"):
        return ParentalRole.MOTHER

    return ParentalRole.UNKNOWN


def map_parent(family_record: FamilyRecord) -> Parent:
    """
    Maps a FamilyRecord instance to a Parent domain model instance.
    """

    family_id = family_record.family_id
    parental_role = parse_parental_role(family_record.padre_madre)
    mutation = family_record.mutazione
    recurrent_fever = map_boolean(family_record.febbre_ricorrente)
    temperature_category = map_temperature_category(family_record.t_max)
    episode_duration = map_episode_duration(family_record.durata)
    abdominal_pain = map_boolean(family_record.dol_addominale)
    chest_pain = map_boolean(family_record.dol_toracico)
    headache = map_boolean(family_record.cefalea)
    osteoarticular_pain = map_boolean(family_record.dol_osteoarticolari)
    aphthosis_with_fever = map_boolean(family_record.aftosi_con_febbre)
    aphthosis_without_fever = map_boolean(family_record.aftosi_senza_febbre)
    erythematous_tonsillitis = map_boolean(family_record.tonsillite_eritematosa)
    exudative_tonsillitis = map_boolean(family_record.tonsillite_essudativa)
    cutaneous_manifestations = map_boolean(family_record.man_cutanee)
    asthenia = map_boolean(family_record.astenia)
    respiratory_infections_chronic = map_boolean(family_record.irc)
    fever_in_adulthood = map_boolean(family_record.febbre_eta_adulta)
    family_amyloidosis = map_boolean(family_record.amiloidosi_famiglia)
    onset_before_18 = map_boolean(family_record.esordio_lt_18)
    onset_after_18 = map_boolean(family_record.esordio_gt_18)
    episodes_per_year = map_int(family_record.episodi_anno) 
    tonsillectomy = map_boolean(family_record.tonsillectomia)
    appendicectomy = map_boolean(family_record.appendicectomia)
    improvement_in_adulthood = map_boolean(family_record.miglioramento_eta_adulta)
    family_respiratory_infections_chronic = map_boolean(family_record.fam_irc)
    consanguinity = map_boolean(family_record.consanguineita)

    return Parent(
        family_id=family_id,
        parental_role=parental_role,
        mutation=mutation,
        recurrent_fever=recurrent_fever,
        temperature_category=temperature_category,
        episode_duration=episode_duration,
        abdominal_pain=abdominal_pain,
        chest_pain=chest_pain,
        headache=headache,
        osteoarticular_pain=osteoarticular_pain,
        aphthosis_with_fever=aphthosis_with_fever,
        aphthosis_without_fever=aphthosis_without_fever,
        erythematous_tonsillitis=erythematous_tonsillitis,
        exudative_tonsillitis=exudative_tonsillitis,
        cutaneous_manifestations=cutaneous_manifestations,
        asthenia=asthenia,
        respiratory_infections_chronic=respiratory_infections_chronic,
        fever_in_adulthood=fever_in_adulthood,
        family_amyloidosis=family_amyloidosis,
        onset_before_18=onset_before_18,
        onset_after_18=onset_after_18,
        episodes_per_year=episodes_per_year,
        tonsillectomy=tonsillectomy,
        appendicectomy=appendicectomy,
        improvement_in_adulthood=improvement_in_adulthood,
        family_respiratory_infections_chronic=family_respiratory_infections_chronic,
        consanguinity=consanguinity
    )