from ..domain.temperature_category import TemperatureCategory
from ..domain.episode_duration import EpisodeDuration
from ..domain.parental_role import ParentalRole
from ..domain.gender import Gender
from ..domain.country import Country
from ..domain.mutation import Mutation
from ..domain.fever_trigger import FeverTrigger
from ..domain.optional_bool import OptionalBool


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
    for t in FeverTrigger:
        if t.value == s:
            return t
    return FeverTrigger.UNKNOWN