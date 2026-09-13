from ..domain.parent import Parent
from ..models.family_record import FamilyRecord
from ..domain.parental_role import ParentalRole

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

    return Parent(
        family_id=family_id,
        parental_role=parental_role
    )