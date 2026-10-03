from datetime import datetime

from ..domain.family import Family
from ..statistics.models.statistics import Statistics
from ..utilities.path_utilities import resolve_style_link, wsl_to_windows_unc
from .family_viewmodel_builder import build_family_viewmodel
from .report_viewmodel import ReportViewModel


def build_report_viewmodel(
    title: str,
    subtitle: str | None = None,
    version: str | None = None,
    author: str | None = None,
    families: list[Family] = None,
    statistics: Statistics | None = None,
    target: str = "pdf",
) -> ReportViewModel:
    """
    Build a ReportViewModel from the given title, subtitle, version, author, families, and statistics.
    """

    if families is None:
        families = []
    family_vms = [build_family_viewmodel(f) for f in families]

    style_links = [
        "bootstrap.min.css",
        "report.css",
        "font-awesome-4.7.0/css/font-awesome.min.css",
    ]

    resolved_style_links = [resolve_style_link(style) for style in style_links]

    if target == "html":
        resolved_style_links = [wsl_to_windows_unc(style) for style in resolved_style_links]

    total_families = len(family_vms)
    total_children = sum(len(f.components) for f in family_vms)

    return ReportViewModel(
        title=title,
        subtitle=subtitle,
        style_links=resolved_style_links,
        version=version,
        families=family_vms,
        statistics=statistics,
        author=author,
        created_at=datetime.now(),
        total_families=total_families,
        total_children=total_children,
    )
