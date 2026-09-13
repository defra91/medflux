from enum import Enum


class FeverTrigger(Enum):
    NONE = "NONE"
    STRESS = "STRESS"
    INFECTION = "INFECTION"
    COLD = "COLD"
    EXERCISE = "EXERCISE"
    UNKNOWN = "UNK"
