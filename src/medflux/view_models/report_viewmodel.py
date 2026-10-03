from dataclasses import dataclass, field
from datetime import datetime

from ..domain.family import Family
from ..statistics.models.statistics import Statistics
from .genetic_variant_distribution import GeneticVariantDistributionVM


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

    style_links: list[str] = field(default_factory=list)

    families: list[Family] = field(default_factory=list)
    statistics: Statistics | None = None

    version: str | None = None
    author: str | None = None
    created_at: datetime = field(default_factory=datetime.now)

    total_families: int | None = None
    total_children: int | None = None

    genetic_variant_distribution: GeneticVariantDistributionVM | None = None
