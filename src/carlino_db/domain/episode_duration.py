from enum import Enum


class EpisodeDuration(Enum):
    LESS_THAN_12H = "<12h"
    BETWEEN_12_AND_72H = "12–72h"
    MORE_THAN_72H = ">72h"
    UNKNOWN = "unknown"
