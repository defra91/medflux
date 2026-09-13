from enum import Enum

class Mucocutaneous(Enum):
    NONE = "None"

    ORAL_APHTHOUS = "Oral Aphtous"
    ORAL_APHTHOUS_CAVITY = "Oral Aphtous Cavity"

    EXUDATIVE_PHARYNGOTONSILLITIS = "Exudative Pharyngotonsillitis"
    ERYTHEMATOUS_PHARYNGOTONSILLITIS = "Erythematous Pharyngotonsillitis"

    ERYSIPELAS = "Erysipelas"
    PHARYNGEAL_HYPEREMIA = "Pharyngeal Hyperemia"
    TONSILLAR_HYPERTROPHY = "Tonsillar Hypertrophy"
    HYPERPIGMENTED_CUTANEOUS_LESIONS = "Hyperpigmented Cutaneous Lesions"

    # Combinations
    APHTHOUS_AND_EXUDATIVE_PHARYNGOTONSILLITIS = "Aphtous and Exudative Pharyngotonsillitis"
    APHTHOUS_ERYSIPELAS_AND_EXUDATIVE_PHARYNGOTONSILLITIS = "Aphtous, Erysipelas and Exudative Pharyngotonsillitis"
    HYPERPIGMENTED_AND_EXUDATIVE_PHARYNGOTONSILLITIS = "Hyperpigmented and Exudative Pharyngotonsillitis"

    UNKNOWN = "Unknown"
