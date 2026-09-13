# src/main.py

from datetime import datetime

from .db import load_family_records, load_patient_records
from .view_models.report_viewmodel import ReportViewModel
from .mappers.parent_mapper import map_parent
from .mappers.child_mapper import map_child

from .reports.renderer import render_family_report
from .reports.pdf import html_to_pdf

from .services.family_builder import build_families

from .statistics.statistics_calculation import calculate_statistics

def main():
    
    family_records = load_family_records()
    patient_records = load_patient_records()

    print(f"Loaded {len(family_records)} family records from the database.")
    print(f"Loaded {len(patient_records)} patient records from the database.")

    parents = []
    children = []

    for family_record in family_records:
        parent = map_parent(family_record)
        parents.append(parent)

    for patient_record in patient_records:
        child = map_child(patient_record)
        children.append(child)

    from .writer import write_json
    write_json(parents, "parents.json")
    write_json(children, "children.json")
    
    families = build_families(children, parents)

    statistics = calculate_statistics(families)

    vm = ReportViewModel(
        title="Children Report",
        subtitle=None,
        families=families,
        created_at=datetime.now(),
        statistics=statistics
    )

    html = render_family_report(vm)
    html_to_pdf(html, "report.pdf")


if __name__ == "__main__":
    main()