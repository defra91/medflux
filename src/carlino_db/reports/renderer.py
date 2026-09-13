from jinja2 import Environment, FileSystemLoader
from pathlib import Path

TEMPLATE_DIR = Path(__file__).parent / "templates"

env = Environment(
    loader=FileSystemLoader(str(TEMPLATE_DIR)),
    autoescape=True
)

def render_family_report(vm) -> str:
    template = env.get_template("family_report.html")
    return template.render(vm=vm)


def yes_no(value):
    return "Yes" if value else "No"


def yes_no_check(value):
    return "<i class='fa fa-check-square-o' aria-hidden='true'></i>" if value else "<i class='fa fa-square-o' aria-hidden='true'></i>"


def days(value):
    return f"{value} days" if value is not None else "N/A"


def format_float(value):
    if value is None:
        return "N/A"
    try:
        # Format: comma as thousands separator, dot as decimal separator
        return f"{value:,.2f}"
    except Exception:
        return str(value)

env.filters["yes_no"] = yes_no
env.filters["days"] = days
env.filters["yes_no_check"] = yes_no_check
env.filters["format_float"] = format_float