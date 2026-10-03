import json
from collections.abc import Iterable
from dataclasses import asdict, is_dataclass
from enum import Enum
from pathlib import Path
from typing import Any

DEBUG_DIR = Path.cwd() / "debug"


def to_serializable(obj: Any) -> Any:
    if is_dataclass(obj):
        return {k: to_serializable(v) for k, v in asdict(obj).items()}

    if hasattr(obj, "model_dump"):
        return {k: to_serializable(v) for k, v in obj.model_dump().items()}

    if isinstance(obj, Enum):
        return obj.value

    if isinstance(obj, (list, tuple)):
        return [to_serializable(v) for v in obj]

    if isinstance(obj, dict):
        return {k: to_serializable(v) for k, v in obj.items()}

    if hasattr(obj, "__dict__"):
        return {k: to_serializable(v) for k, v in obj.__dict__.items()}

    return obj


def write_json(objects: Iterable[Any], filename: str) -> None:
    DEBUG_DIR.mkdir(exist_ok=True)

    serializable = []

    for obj in objects:
        data = to_serializable(obj)
        serializable.append(data)

    with open(DEBUG_DIR / filename, "w", encoding="utf-8") as f:
        json.dump(serializable, f, indent=2, ensure_ascii=False)
