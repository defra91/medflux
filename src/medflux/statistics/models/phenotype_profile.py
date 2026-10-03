from dataclasses import dataclass


@dataclass
class PhenotypeProfile:
    """
    Profilo fenotipico di un individuo.
    symptoms: dict con sintomo -> True/False
    """

    symptoms: dict[str, bool]
