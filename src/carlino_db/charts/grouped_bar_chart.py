from __future__ import annotations

from collections.abc import Sequence
from pathlib import Path

from matplotlib import pyplot as plt
from matplotlib.figure import Figure

from .base import BaseChart


class GroupedBarChart(BaseChart):
    """Grouped bar chart builder."""

    def __init__(
        self,
        labels: Sequence[str],
        series: Sequence[tuple[str, Sequence[float]]],
        title: str | None = None,
        *,
        xlabel: str | None = None,
        ylabel: str | None = None,
        colors: Sequence[str] | None = None,
        rotation: int = 90,
    ):
        self.series = [
            (series_name, list(values)) for series_name, values in series
        ]
        self.colors = list(colors) if colors is not None else None
        super().__init__(labels, [0 for _ in labels], title, xlabel=xlabel, ylabel=ylabel)
        self.rotation = rotation

        if any(len(values) != len(labels) for _, values in self.series):
            raise ValueError("Each series must contain one value for every label.")

        if self.colors is not None and len(self.colors) != len(self.series):
            raise ValueError("Colors must match the number of series.")

    def build_figure(self) -> Figure:
        fig, ax = plt.subplots(figsize=(9, 7))
        x_positions = range(len(self.labels))
        group_width = 0.8
        bar_width = group_width / max(len(self.series), 1)
        gap = 0.08

        for index, (series_name, values) in enumerate(self.series):
            offset = (index - (len(self.series) - 1) / 2) * (bar_width + gap)
            color = self.colors[index] if self.colors is not None else None
            bars = ax.bar(
                [position + offset for position in x_positions],
                values,
                width=bar_width,
                label=series_name,
                color=color,
            )
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

        ax.set_xticks(list(x_positions))
        ax.set_xticklabels(self.labels, rotation=self.rotation)
        ax.set_title(self.title)

        if self.xlabel is not None:
            ax.set_xlabel(self.xlabel)
        if self.ylabel is not None:
            ax.set_ylabel(self.ylabel)

        ax.legend()
        fig.tight_layout()
        return fig


def build_grouped_bar_chart(
    labels: Sequence[str],
    series: Sequence[tuple[str, Sequence[float]]],
    title: str | None = None,
    *,
    xlabel: str | None = None,
    ylabel: str | None = None,
    colors: Sequence[str] | None = None,
    rotation: int = 90,
) -> Figure:
    return GroupedBarChart(labels, series, title, xlabel=xlabel, ylabel=ylabel, colors=colors, rotation=rotation).build_figure()


def save_grouped_bar_chart(
    labels: Sequence[str],
    series: Sequence[tuple[str, Sequence[float]]],
    output_path: str | Path,
    title: str | None = None,
    *,
    xlabel: str | None = None,
    ylabel: str | None = None,
    colors: Sequence[str] | None = None,
    dpi: int = 150,
    transparent: bool = False,
) -> Path:
    chart = GroupedBarChart(labels, series, title, xlabel=xlabel, ylabel=ylabel, colors=colors, rotation=90)
    return chart.save(output_path, dpi=dpi, transparent=transparent)
