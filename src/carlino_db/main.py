import logging
from datetime import datetime
from pathlib import Path

from .db import load_family_records, load_patient_records
from .view_models.report_viewmodel import ReportViewModel
from .mappers.parent_mapper import map_parent
from .mappers.child_mapper import map_child

from .reports.renderer import render_family_report
from .reports.pdf import html_to_pdf

from .services.family_builder import build_families
from .statistics.statistics_calculation import calculate_statistics


def main(db_path: Path, output_path: Path, verbose: bool = False, debug: bool = False):
    """
    Main entry point for the Carlino DB processing pipeline.
    """

    # Configure logging
    logging.basicConfig(
        level=logging.DEBUG if verbose else logging.INFO,
        format="%(asctime)s [%(levelname)s] %(message)s"
    )

    logging.info("Starting Carlino DB processing pipeline...")
    logging.info(f"Database path: {db_path}")
    logging.info(f"Output path: {output_path}")

    # Load raw records
    family_records = load_family_records(db_path)
    patient_records = load_patient_records(db_path)

    logging.info(f"Loaded {len(family_records)} family records.")
    logging.info(f"Loaded {len(patient_records)} patient records.")

    # Map raw records to domain objects
    parents = [map_parent(fr) for fr in family_records]
    children = [map_child(pr) for pr in patient_records]

    # Debug export
    if debug:
        logging.debug("Debug mode enabled: exporting raw mapped JSON files.")
        from .writer import write_json
        write_json(parents, "parents.json")
        write_json(children, "children.json")

    # Build Family objects
    families = build_families(children, parents)
    logging.info(f"Built {len(families)} Family objects.")

    # Compute statistics
    statistics = calculate_statistics(families)
    logging.info("Statistics computed successfully.")

    # Build view model
    vm = ReportViewModel(
        title="Children Report",
        subtitle=None,
        families=families,
        statistics=statistics,
        created_at=datetime.now(),
    )

    # Render HTML and convert to PDF
    logging.info("Rendering HTML report...")
    html = render_family_report(vm)

    logging.info("Generating PDF...")
    html_to_pdf(html, output_path)

    logging.info("Report generation completed successfully.")
