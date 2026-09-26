from datetime import datetime
from pathlib import Path

from ..domain.family import Family
from ..statistics.models.statistics import Statistics
from .family_viewmodel_builder import build_family_viewmodel
from .report_viewmodel import ReportViewModel


def wsl_to_windows_unc(path: str, distro: str = "Ubuntu") -> str:
    """
    Converte un path WSL in un path UNC Windows accessibile via \\wsl$.
    Esempio:
        /home/lucad/file.txt
    diventa:
        \\wsl$\\Ubuntu\\home\\lucad\\file.txt
    """
    p = Path(path)

    # Normalizza il path in stringa
    s = str(p)

    # Rimuove eventuali prefissi strani (./, ../)
    s = s.replace("\\", "/")

    # Assicura che sia un path assoluto WSL
    if not s.startswith("/"):
        raise ValueError(f"Il path non è un path WSL assoluto: {s}")

    # Costruzione UNC
    unc = f"\\\\wsl$\\{distro}" + s.replace("/", "\\")
    return unc



def resolve_style_link(style: str) -> Path:
    # Implement the logic to resolve the full path or URL for the given style

    templates_dir = Path.cwd() / "src" / "carlino_db" / "reports" / "templates"
    style_path = templates_dir / style

    if style_path.exists():
        return style_path
    else:
        return Path(style)


def build_report_viewmodel(
        title: str,
        subtitle: str | None = None,
        version: str | None = None,
        author: str | None = None,
        families: list[Family] = None,
        statistics: Statistics | None = None,
        target: str = "pdf") -> ReportViewModel:
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

    return ReportViewModel(
        title=title,
        subtitle=subtitle,
        style_links=resolved_style_links,
        version=version,
        families=family_vms,
        statistics=statistics,
        author=author,
        created_at=datetime.now(),
    )
