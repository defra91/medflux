import logging
from pathlib import Path

from .db import load_family_records, load_patient_records
from .mappers.child_mapper import map_child
from .mappers.parent_mapper import map_parent
from .reports.pdf import html_to_pdf
from .reports.renderer import render_family_report
from .services.family_builder import build_families
from .statistics.statistics_calculation import calculate_statistics
from .utilities.style_utilities import compile_sass
from .view_models.report_viewmodel_builder import build_report_viewmodel


def _build_report_viewmodel(families, statistics, target: str):
    title = "Rapporto di valutazione genetica familiare"
    subtitle = "Analisi delle mutazioni, dei fenotipi e delle relazioni familiari"
    version = "1.0"
    author = "Mariagrazia Carlino"

    return build_report_viewmodel(
        title=title,
        subtitle=subtitle,
        version=version,
        author=author,
        families=families,
        statistics=statistics,
        target=target,
    )


def main(db_path: Path, output_path: Path, verbose: bool = False, debug: bool = False):
    """
    Main entry point for the Medflux processing pipeline.
    """

    # Configure logging
    logging.basicConfig(
        level=logging.DEBUG if verbose else logging.ERROR, format="%(asctime)s [%(levelname)s] %(message)s"
    )

    logging.info("Starting Medflux processing pipeline...")
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

    children_with_abdominal_pain = [child for child in children if child.abdominal_pain]
    logging.info(f"Found {len(children_with_abdominal_pain)} children with abdominal pain.")
    parents_with_abdominal_pain = [parent for parent in parents if parent.abdominal_pain]
    logging.info(f"Found {len(parents_with_abdominal_pain)} parents with abdominal pain.")

    # Build Family objects
    families = build_families(children, parents)
    logging.info(f"Built {len(families)} Family objects.")

    # Compute statistics
    statistics = calculate_statistics(families)
    logging.info("Statistics computed successfully.")

    # Build view model
    vm = _build_report_viewmodel(families=families, statistics=statistics, target="pdf")

    # Build sass
    compile_sass()

    # Render HTML and convert to PDF
    logging.info("Rendering HTML report...")
    html = render_family_report(vm)

    # Debug export
    if debug:
        logging.debug("Debug mode enabled: exporting raw mapped JSON files.")
        from .writer import write_json

        write_json(parents, "parents.json")
        write_json(children, "children.json")
        write_json(families, "families.json")

    if debug:
        vm_debug = _build_report_viewmodel(families=families, statistics=statistics, target="html")
        html_debug = render_family_report(vm_debug)
        logging.debug("Exporting rendered HTML for debugging purposes.")
        with open("report.html", "w") as f:
            f.write(html_debug)

    logging.info("Generating PDF...")
    html_to_pdf(html, output_path)

    logging.info("Report generation completed successfully.")
