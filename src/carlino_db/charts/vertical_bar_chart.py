from __future__ import annotations

from collections.abc import Sequence
from pathlib import Path

from matplotlib import pyplot as plt
from matplotlib.figure import Figure

from .base import BaseChart


class VerticalBarChart(BaseChart):
    """Vertical bar chart builder."""

    def __init__(
        self,
        labels: Sequence[str],
        values: Sequence[float],
        title: str = "Vertical bar chart",
        *,
        xlabel: str | None = None,
        ylabel: str | None = None,
        color: str = "#4c78a8",
    ):
        self.color = color
        super().__init__(labels, values, title, xlabel=xlabel, ylabel=ylabel)

    def build_figure(self) -> Figure:
        fig, ax = plt.subplots(figsize=(9, 7))
        ax.bar(self.labels, self.values, color=self.color)
        ax.set_title(self.title)

        if self.xlabel is not None:
            ax.set_xlabel(self.xlabel)
        if self.ylabel is not None:
            ax.set_ylabel(self.ylabel)

        fig.tight_layout()
        return fig


def build_vertical_bar_chart(
    labels: Sequence[str],
    values: Sequence[float],
    title: str = "Vertical bar chart",
    *,
    xlabel: str | None = None,
    ylabel: str | None = None,
    color: str = "#4c78a8",
) -> Figure:
    return VerticalBarChart(labels, values, title, xlabel=xlabel, ylabel=ylabel, color=color).build_figure()


def save_vertical_bar_chart(
    labels: Sequence[str],
    values: Sequence[float],
    output_path: str | Path,
    title: str = "Vertical bar chart",
    *,
    xlabel: str | None = None,
    ylabel: str | None = None,
    color: str = "#4c78a8",
    dpi: int = 150,
    transparent: bool = False,
) -> Path:
    chart = VerticalBarChart(labels, values, title, xlabel=xlabel, ylabel=ylabel, color=color)
    return chart.save(output_path, dpi=dpi, transparent=transparent)
