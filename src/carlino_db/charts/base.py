from __future__ import annotations

from collections.abc import Sequence
from pathlib import Path

import matplotlib
from matplotlib import pyplot as plt
from matplotlib.figure import Figure

matplotlib.use("Agg")


class BaseChart:
    """Base class with utilities for saving chart images."""

    def __init__(
            self,
            labels: Sequence[str],
            values: Sequence[float],
            title: str, *,
            xlabel: str | None = None,
            ylabel: str | None = None):
        self.labels = list(labels)
        self.values = list(values)
        self.title = title
        self.xlabel = xlabel
        self.ylabel = ylabel

        self._validate_inputs()

    def _validate_inputs(self) -> None:
        if not self.labels:
            raise ValueError("At least one label is required.")

        if len(self.labels) != len(self.values):
            raise ValueError("Labels and values must have the same length.")

        if not self.values:
            raise ValueError("At least one value is required.")

    def build_figure(self) -> Figure:
        raise NotImplementedError("Subclasses must implement build_figure().")

    @staticmethod
    def _resolve_output_path(output_path: str | Path) -> Path:
        path = Path(output_path)
        if path.suffix == "":
            path = path.with_suffix(".png")
        path.parent.mkdir(parents=True, exist_ok=True)
        return path

    def save(self, output_path: str | Path, *, dpi: int = 150, transparent: bool = False) -> Path:
        figure = self.build_figure()
        destination = self._resolve_output_path(output_path)
        figure.savefig(destination, dpi=dpi, bbox_inches="tight", transparent=transparent)
        plt.close(figure)
        return destination
