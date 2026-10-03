# Medflux

Medflux is a Python tool for processing family clinical and genetic data and producing professional PDF reports and publication-ready charts. It provides a single CLI pipeline that transforms input data into a formatted report and exports charts as PNG files.

This project is open-source and released under the MIT License. See the LICENSE file for details.

Key features
- End-to-end pipeline: read data, compute statistics, render HTML templates, and generate PDF reports.
- Built-in statistical helpers for families, parents, children, and mutation-focused summaries.
- Reusable chart builders that export PNGs (horizontal, vertical, grouped bar charts, and pie charts).
- Templating with Jinja and SCSS-based styling for customizable report layouts.
- CLI-first design with a single entry point for pipelines and reporting.

Requirements
- Python 3.14 or newer
- uv (https://docs.astral.sh/uv/) for dependency and environment management

Installation
1. Install uv (if not already installed) and sync dependencies:

```bash
uv sync
```

CLI usage
Run the main pipeline with:

```bash
uv run medflux --db-path /path/to/database.xlsx --output-path output/report.pdf
```

Common flags
- -v, --verbose    Enable verbose logging
- -g, --debug      Export debug artifacts (e.g. parents.json, children.json, families.json, report.html)

Chart API (example)
Use the chart helpers to create and save PNG charts:

```python
from pathlib import Path
from medflux.charts import save_horizontal_bar_chart, save_vertical_bar_chart, save_grouped_bar_chart, save_pie_chart

out = Path('output')
out.mkdir(parents=True, exist_ok=True)

save_horizontal_bar_chart(labels=['A','B','C'], values=[12,18,9], output_path=out / 'h.png', title='Horizontal')
save_vertical_bar_chart(labels=['A','B','C'], values=[12,18,9], output_path=out / 'v.png', title='Vertical')
save_grouped_bar_chart(labels=['S1','S2'], series=[('P',[3,4]),('C',[5,6])], output_path=out / 'grouped.png', title='Grouped')
save_pie_chart(labels=['m1','m2'], values=[60,40], output_path=out / 'pie.png', title='Mutations')
```

Project layout

```text
src/medflux/
  charts/        # chart builders and save helpers
  statistics/    # statistical calculators and chart assembly
  reports/       # templates, styles, and PDF generation
  mappers/       # record -> domain mapping
  domain/        # core domain models
  view_models/   # report view models
  cli.py         # CLI entry point
  main.py        # pipeline orchestration
```

Development
- Lint: `uv run ruff check .`
- Format check: `uv run black --check src tests`
- Tests: `uv run --with pytest pytest -q`

Notes
- Chart images created by the pipeline are saved under `chart_images_results/`.
- SCSS styles are compiled as part of report generation and can be customized in `src/medflux/reports/`.

License
This project is open-source and released under the MIT License. See the LICENSE file for details.
