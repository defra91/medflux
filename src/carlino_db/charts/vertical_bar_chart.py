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
        rotation: int = 90,
    ):
        self.color = color
        self.rotation = rotation
        super().__init__(labels, values, title, xlabel=xlabel, ylabel=ylabel)

    def build_figure(self) -> Figure:
        fig, ax = plt.subplots(figsize=(9, 7))
        bars = ax.bar(self.labels, self.values, color=self.color)
        ax.set_title(self.title)

        if self.xlabel is not None:
            ax.set_xlabel(self.xlabel)
        if self.ylabel is not None:
            ax.set_ylabel(self.ylabel)

        ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda value, _pos: f"{int(value)}"))

        for bar in bars:
            height = bar.get_height()
            ax.text(
                bar.get_x() + bar.get_width() / 2,
                height + 0.05,
                f"{int(height)}",
                ha="center",
                va="bottom",
                fontsize=9,
            )

        plt.setp(ax.get_xticklabels(), rotation=self.rotation, ha="right", rotation_mode="anchor")
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
    rotation: int = 90,
) -> Figure:
    return VerticalBarChart(labels, values, title, xlabel=xlabel, ylabel=ylabel, color=color, rotation=rotation).build_figure()


def save_vertical_bar_chart(
    labels: Sequence[str],
    values: Sequence[float],
    output_path: str | Path,
    title: str = "Vertical bar chart",
    *,
    xlabel: str | None = None,
    ylabel: str | None = None,
    color: str = "#4c78a8",
    rotation: int = 90,
    dpi: int = 150,
    transparent: bool = False,
) -> Path:
    chart = VerticalBarChart(labels, values, title, xlabel=xlabel, ylabel=ylabel, color=color, rotation=rotation)
    return chart.save(output_path, dpi=dpi, transparent=transparent)
