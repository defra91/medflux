from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional, List

from ..statistics.models.statistics import Statistics
from ..domain.family import Family


@dataclass
class ReportViewModel:
    """
    ViewModel per la generazione del report HTML/PDF.
    Contiene:
    - titolo e sottotitolo del documento
    - lista delle famiglie (dati grezzi)
    - statistiche calcolate (opzionali)
    - timestamp di creazione
    """
    title: str
    subtitle: Optional[str] = None

    families: List[Family] = field(default_factory=list)
    statistics: Optional[Statistics] = None

    created_at: datetime = field(default_factory=datetime.now)
