import logging
from pathlib import Path

import sass

BASE_DIR = Path(__file__).resolve().parent.parent
STYLES_DIR = BASE_DIR / "reports" / "templates" / "styles"
TPL_DIR = BASE_DIR / "reports" / "templates"


def compile_sass():
    """
    Compiles the main SASS file into a CSS file and writes it to the templates directory.
    """

    input_scss = STYLES_DIR / "style.scss"
    output_css = TPL_DIR / "report.css"

    css = sass.compile(filename=str(input_scss))

    output_css.write_text(css, encoding="utf-8")

    logging.info(f"🎨 CSS generated: {output_css}")
