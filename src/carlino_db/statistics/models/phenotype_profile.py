from dataclasses import dataclass
from typing import Dict

@dataclass
class PhenotypeProfile:
    """
    Profilo fenotipico di un individuo.
    symptoms: dict con sintomo -> True/False
    """
    symptoms: Dict[str, bool]