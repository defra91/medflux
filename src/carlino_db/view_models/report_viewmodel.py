from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional, List
from ..statistics.statistics import Statistics
from ..domain.family import Family


@dataclass
class ReportViewModel:
    title: str
    subtitle: Optional[str]
    families: List[Family]
    statistics: Optional[Statistics]

    created_at: datetime = field(default_factory=datetime.now)