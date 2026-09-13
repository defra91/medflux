from ..domain.temperature_category import TemperatureCategory
from ..domain.episode_duration import EpisodeDuration

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
