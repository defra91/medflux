from __future__ import annotations

from collections.abc import Sequence
from pathlib import Path

from matplotlib import pyplot as plt
from matplotlib.figure import Figure

from .base import BaseChart


class PieChart(BaseChart):
    """Pie chart builder."""

    def __init__(
        self,
        labels: Sequence[str],
        values: Sequence[float],
        title: str | None = None,
        *,
        xlabel: str | None = None,
        ylabel: str | None = None,
        colors: Sequence[str] | None = None,
    ):
        self.colors = list(colors) if colors is not None else None
        super().__init__(labels, values, title, xlabel=xlabel, ylabel=ylabel)

        if self.colors is not None and len(self.colors) != len(self.labels):
            raise ValueError("Colors must match the number of labels.")

    def build_figure(self) -> Figure:
        fig, ax = plt.subplots(figsize=(8, 8))

        if self.colors is not None:
            ax.pie(self.values, labels=self.labels, autopct="%1.1f%%", colors=self.colors)
        else:
            ax.pie(self.values, labels=self.labels, autopct="%1.1f%%")

        ax.set_title(self.title)
        fig.tight_layout()
        return fig


def build_pie_chart(
    labels: Sequence[str],
    values: Sequence[float],
    title: str | None = None,
    *,
    xlabel: str | None = None,
    ylabel: str | None = None,
    colors: Sequence[str] | None = None,
) -> Figure:
    return PieChart(labels, values, title, xlabel=xlabel, ylabel=ylabel, colors=colors).build_figure()


def save_pie_chart(
    labels: Sequence[str],
    values: Sequence[float],
    output_path: str | Path,
    title: str | None = None,
    *,
    xlabel: str | None = None,
    ylabel: str | None = None,
    colors: Sequence[str] | None = None,
    dpi: int = 150,
    transparent: bool = False,
) -> Path:
    chart = PieChart(labels, values, title, xlabel=xlabel, ylabel=ylabel, colors=colors)
    return chart.save(output_path, dpi=dpi, transparent=transparent)
