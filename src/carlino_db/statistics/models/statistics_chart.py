from dataclasses import dataclass


@dataclass
class StatisticsChart:
    """Data class representing a rendered chart in the statistics module."""

    title: str
    description: str | None = None
    image_url: str | None = None
