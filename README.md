# MedFlux

Questo progetto contiene un pipeline per la generazione di report e, ora, anche API dedicate per la costruzione e il salvataggio di grafici.

## Grafici supportati

- Istogrammi orizzontali
- Istogrammi verticali
- Grafici a torta

## Esempio di utilizzo

```python
from pathlib import Path

from carlino_db.charts import (
    save_horizontal_bar_chart,
    save_pie_chart,
    save_vertical_bar_chart,
)

save_horizontal_bar_chart(
    labels=["A", "B", "C"],
    values=[12, 18, 9],
    output_path=Path("output/horizontal.png"),
    title="Valori per categoria",
    xlabel="Valore",
    ylabel="Categoria",
)

save_vertical_bar_chart(
    labels=["A", "B", "C"],
    values=[12, 18, 9],
    output_path=Path("output/vertical.png"),
    title="Valori per categoria",
)

save_pie_chart(
    labels=["A", "B", "C"],
    values=[25, 50, 25],
    output_path=Path("output/pie.png"),
    title="Distribuzione",
)
```

Le funzioni di salvataggio creano automaticamente la directory di destinazione e salvano l'immagine in formato PNG.
