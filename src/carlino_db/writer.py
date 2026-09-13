from pathlib import Path
import json
from typing import Any, Iterable
from .config import OUTPUT_DIR
from enum import Enum


def write_json(objects: Iterable[Any], filename: str) -> None:
    OUTPUT_DIR.mkdir(exist_ok=True)

    serializable = []

    for obj in objects:
        # Pydantic
        if hasattr(obj, "model_dump"):
            data = obj.model_dump()

        # Dataclass / oggetto normale
        elif hasattr(obj, "__dict__"):
            data = obj.__dict__

        else:
            raise TypeError(
                f"Impossibile serializzare oggetto di tipo {type(obj)}: "
                "manca model_dump() o __dict__"
            )

        # Convert enum to their values for JSON serialization
        for key, value in data.items():
            if isinstance(value, Enum):
                data[key] = value.value

        serializable.append(data)

    with open(OUTPUT_DIR / filename, "w", encoding="utf-8") as f:
        json.dump(serializable, f, indent=2, ensure_ascii=False)
