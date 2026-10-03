from pathlib import Path


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
