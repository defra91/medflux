from pathlib import Path
import json
from typing import Any, Iterable
from .config import OUTPUT_DIR


def write_json(objects: Iterable[Any], filename: str) -> None:
    OUTPUT_DIR.mkdir(exist_ok=True)

    serializable = []

    for obj in objects:
        # Pydantic
        if hasattr(obj, "model_dump"):
            serializable.append(obj.model_dump())

        # Dataclass o oggetto normale
        elif hasattr(obj, "__dict__"):
            serializable.append(obj.__dict__)

        else:
            raise TypeError(f"Impossible to serialize object of type {type(obj)}")

    with open(OUTPUT_DIR / filename, "w", encoding="utf-8") as f:
        json.dump(serializable, f, indent=2, ensure_ascii=False)
