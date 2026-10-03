# src/medflux/normalization.py

import math
from typing import Any


def normalize_cell_value(v: Any) -> str | None:
    """
    Converte qualsiasi valore Excel in stringa.
    Celle vuote (NaN) diventano None.
    """

    # NaN → None
    if isinstance(v, float) and math.isnan(v):
        return None

    # None → None
    if v is None:
        return None

    # Tutto il resto → stringa ripulita
    return str(v).strip()
