from pathlib import Path
from weasyprint import HTML

def html_to_pdf(html: str, output_path: str):
    templates_dir = Path(__file__).parent / "templates"

    HTML(
        string=html,
        base_url=str(templates_dir)
    ).write_pdf(output_path)
