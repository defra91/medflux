from dataclasses import dataclass, field
from datetime import datetime

from ..domain.family import Family
from ..statistics.models.statistics import Statistics


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
    subtitle: str | None = None

    families: list[Family] = field(default_factory=list)
    statistics: Statistics | None = None

    created_at: datetime = field(default_factory=datetime.now)
