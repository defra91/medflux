from ..domain.temperature_category import TemperatureCategory
from ..domain.episode_duration import EpisodeDuration
from ..domain.parental_role import ParentalRole
from ..domain.gender import Gender
from ..domain.country import Country
from ..domain.mutation import Mutation
from ..domain.fever_trigger import FeverTrigger
from ..domain.optional_bool import OptionalBool
from ..domain.abdominal_surgery import AbdominalSurgery
from ..domain.mucocutaneous import Mucocutaneous
from ..domain.therapy_response import TherapyResponse
from ..domain.collateral_effects import CollateralEffects
from ..domain.amyloidosis import Amyloidosis

def map_str(raw: str | None) -> str | None:
    if raw is None:
        return None
    s = raw.strip()
    return s if s else None


def map_float(raw: str | None) -> float | None:
    if raw is None:
        return None
    s = raw.strip().replace(",", ".")
    try:
        return float(s)
    except ValueError:
        return None



def map_boolean(value: str | None) -> bool | None:
    """
    Maps a string representation of a boolean value to a Python boolean.
    Returns None if the input is None or cannot be interpreted as a boolean.
    """
    if value is None:
        return None

    s = value.strip().upper()

    if s in ("1", "1.0", "YES", "Y", "TRUE", "T", "SI", "S", "SÌ"):
        return True

    if s in ("0", "0.0", "NO", "N", "FALSE", "F"):
        return False

    return None


def map_optional_bool(value: str | None) -> OptionalBool | None:
    """
    Maps a string representation of an optional boolean value to an OptionalBool enum.
    Returns None if the input is None or cannot be interpreted as an optional boolean.
    """
    if value is None:
        return None

    s = value.strip().upper()

    if s in ("1", "1.0", "YES", "Y", "TRUE", "T", "SI", "S", "SÌ"):
        return OptionalBool.TRUE
    
    if s in ("0", "0.0", "NO", "N", "FALSE", "F"):
        return OptionalBool.FALSE

    return OptionalBool.UNKNOWN


def map_int(raw: str | None) -> int | None:
    """
    Convert raw numeric values into an integer.
    Returns None for missing, unknown, or invalid values.
    """

    if raw is None:
        return None

    s = raw.strip()

    # Handle common 'unknown' markers
    if s.upper() in ("NC", "N.C.", "NA", "N/A", ""):
        return None

    # Try converting to integer
    try:
        return int(s)
    except ValueError:
        return None


def map_temperature_category(raw: str | None) -> TemperatureCategory:
    if raw is None:
        return TemperatureCategory.NOT_PRESENT

    s = raw.strip()

    if s == "0" or s == "0.0":
        return TemperatureCategory.BELOW_38

    if s == "1" or s == "1.0":
        return TemperatureCategory.ABOVE_OR_EQUAL_38

    # include also dirty cases like "99", "", "NC"
    return TemperatureCategory.NOT_PRESENT


def map_episode_duration(raw: str | None) -> EpisodeDuration:
    if raw is None:
        return EpisodeDuration.UNKNOWN

    s = raw.strip()

    if s == "0" or s == "0.0":
        return EpisodeDuration.LESS_THAN_12H

    if s == "1" or s == "1.0":
        return EpisodeDuration.BETWEEN_12_AND_72H

    if s == "2" or s == "2.0":
        return EpisodeDuration.MORE_THAN_72H

    # include 99, NC, "", ecc.
    return EpisodeDuration.UNKNOWN


def map_parental_role(raw: str | None) -> ParentalRole:
    if raw is None:
        return ParentalRole.UNKNOWN

    s = raw.strip().upper()

    if s in ("1", "1.0", "PADRE", "FATHER", "P"):
        return ParentalRole.FATHER

    if s in ("2", "2.0", "MADRE", "MOTHER", "M"):
        return ParentalRole.MOTHER

    return ParentalRole.UNKNOWN


def map_gender(raw: str | None) -> Gender | None:
    if raw is None:
        return Gender.UNKNOWN

    s = raw.strip().upper()

    if s in ("1", "1.0", "M", "MASCHIO"):
        return Gender.MALE

    if s in ("0", "0.0", "F", "FEMMINA"):
        return Gender.FEMALE

    # Covers NC, empty strings, malformed values
    return Gender.UNKNOWN


def map_country(raw: str | None) -> Country | None:
    if raw is None:
        return None

    s = raw.strip().upper()

    if s in ("1", "1.0", "ITALIA"):
        return Country.ITALY

    if s in ("0", "0.0", "ESTERO"):
        return Country.ABROAD

    # Covers NC, empty strings, malformed values
    return Country.UNKNOWN


def map_mutation(raw: str | None) -> Mutation:
    if raw is None:
        return Mutation.UNKNOWN
    s = raw.strip().upper()
    for m in Mutation:
        if m.value == s:
            return m
    return Mutation.UNKNOWN


def map_fever_trigger(raw: str | None) -> FeverTrigger:
    if raw is None:
        return FeverTrigger.UNKNOWN
    s = raw.strip().upper()

    if s in ("NC", "N.C.", "N/A", "NA", ""):
        return FeverTrigger.NC

    if s in ("NO", "N", "NONE"):
        return FeverTrigger.NO

    if s in ("MESTRUAZIONE", "MESTRUAZIONI", "MENSTRUATION", "MENSTRUATIONS"):
        return FeverTrigger.MENSTRUATION

    for t in FeverTrigger:
        if t.value == s:
            return t
    return FeverTrigger.UNKNOWN


def map_abdominal_surgery(raw: str | None) -> AbdominalSurgery:
    if raw is None:
        return AbdominalSurgery.NONE

    s = raw.strip().upper()

    if s in ("NO", "N", "", "NONE"):
        return AbdominalSurgery.NONE

    parts = [p.strip() for p in s.split(",") if p.strip()]

    if parts == ["APPENDICECTOMIA"]:
        return AbdominalSurgery.APPENDICECTOMY

    if parts == ["COLECISTECTOMIA"]:
        return AbdominalSurgery.CHOLECYSTECTOMY

    if set(parts) == {"APPENDICECTOMIA", "COLECISTECTOMIA"}:
        return AbdominalSurgery.APPENDICECTOMY_AND_CHOLECYSTECTOMY

    # Qualsiasi altro valore
    return AbdominalSurgery.UNKNOWN


def normalize_mucocutaneous_token(token: str) -> str:
    t = token.strip().upper()

    t = t.replace("AFOTSI", "AFTOSI")
    t = t.replace("AFOTSI DEL CAVO ORALE", "AFTOSI CAVO ORALE")
    t = t.replace("ERIPISELA", "ERISIPELA")

    t = t.replace("FARINGOTONSILLITI", "FARINGOTONSILLITE")
    t = t.replace("CUTANEA IPERCROMICHE DIFFUSE", "MANIFESTAZIONI CUTANEA IPERCROMICHE DIFFUSE")

    return t


def map_mucocutaneous(raw: str | None) -> Mucocutaneous:
    if raw is None:
        return Mucocutaneous.NONE

    s = raw.strip().upper()

    if s in ("NO", "N", "", "NONE"):
        return Mucocutaneous.NONE

    parts = [normalize_mucocutaneous_token(p) for p in s.split(",") if p.strip()]
    pset = set(parts)

    if pset == {"AFTOSI ORALE"}:
        return Mucocutaneous.ORAL_APHTHOUS

    if pset == {"AFTOSI CAVO ORALE"}:
        return Mucocutaneous.ORAL_APHTHOUS_CAVITY

    if pset == {"FARINGOTONSILLITE ESSUDATIVA"}:
        return Mucocutaneous.EXUDATIVE_PHARYNGOTONSILLITIS

    if pset == {"FARINGOTONSILLITE ERITEMATOSA"}:
        return Mucocutaneous.ERYTHEMATOUS_PHARYNGOTONSILLITIS

    if pset == {"ERISIPELA"}:
        return Mucocutaneous.ERYSIPELAS

    if pset == {"IPEREMIA FARINGEA"}:
        return Mucocutaneous.PHARYNGEAL_HYPEREMIA

    if pset == {"IPERTROFIA TONSILLARE"}:
        return Mucocutaneous.TONSILLAR_HYPERTROPHY

    if pset == {"MANIFESTAZIONI CUTANEA IPERCROMICHE DIFFUSE"}:
        return Mucocutaneous.HYPERPIGMENTED_CUTANEOUS_LESIONS

    if pset == {"AFTOSI ORALE", "FARINGOTONSILLITE ESSUDATIVA"}:
        return Mucocutaneous.APHTHOUS_AND_EXUDATIVE_PHARYNGOTONSILLITIS

    if pset == {"AFTOSI ORALE", "ERISIPELA", "FARINGOTONSILLITE ESSUDATIVA"}:
        return Mucocutaneous.APHTHOUS_ERYSIPELAS_AND_EXUDATIVE_PHARYNGOTONSILLITIS

    if pset == {"MANIFESTAZIONI CUTANEA IPERCROMICHE DIFFUSE", "FARINGOTONSILLITE ESSUDATIVA"}:
        return Mucocutaneous.HYPERPIGMENTED_AND_EXUDATIVE_PHARYNGOTONSILLITIS

    return Mucocutaneous.UNKNOWN


def map_therapy_response(raw: str | None) -> TherapyResponse:
    """
    Map a raw string to a TherapyResponse enum value.
    """
    if raw is None:
        return TherapyResponse.UNKNOWN

    normalized = raw.strip().upper()

    if normalized in ("NO", "N", "NONE"):
        return TherapyResponse.NO

    if normalized in ("YES", "Y"):
        return TherapyResponse.YES

    if normalized in ("SUBOPTIMAL", "SUB-OPTIMAL", "SUBOPTIMAL RESPONSE", "SUB-OPTIMAL RESPONSE", "SUB"):
        return TherapyResponse.SUBOPTIMAL

    return TherapyResponse.UNKNOWN


def map_collateral_effects(raw: str | None) -> CollateralEffects:
    """
    Map a raw string to a CollateralEffects enum value.
    """
    if raw is None:
        return CollateralEffects.UNKNOWN

    normalized = raw.strip().upper()

    if normalized in ("NO", "N", "NONE"):
        return CollateralEffects.NO

    if normalized in ("YES", "Y"):
        return CollateralEffects.YES

    if normalized in ("SI; INTOLL E NON RESPONSIVA", "INTOLLERANT AND NOT RESPONSIVE", "INTOLLERANT & NOT RESPONSIVE", "INTOLLERANT"):
        return CollateralEffects.INTOLLERANT_AND_NOT_RESPONSIVE

    return CollateralEffects.UNKNOWN


def map_amyloidosis(raw: str | None) -> Amyloidosis:
    """
    Map a raw string to an Amyloidosis enum value.
    """
    if raw is None:
        return Amyloidosis.UNKNOWN

    normalized = raw.strip().upper()

    if normalized in ("NO", "N", "NONE"):
        return Amyloidosis.NO

    if normalized in ("YES", "Y"):
        return Amyloidosis.YES

    if normalized in ("DIARRHEA", "DIARREA"):
        return Amyloidosis.DIARRHEA

    if normalized in ("DIARREA,  PIROSI RETROST, CALO PONDERALE"):
        return Amyloidosis.DIARRHEA_RETROSTERNAL_HEARTBURN_WEIGHT_LOSS

    return Amyloidosis.UNKNOWN


def map_family_id(raw_id: str | None) -> str | None:
    if raw_id is None:
        return None

    if "-" not in raw_id:
        return raw_id

    base, suffix = raw_id.rsplit("-", 1)

    if suffix in {"P", "M", "F", "P1", "P2", "P3"}:
        return base

    return raw_id