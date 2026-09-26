from dataclasses import dataclass

@dataclass
class AgeGroupCount:
    """Conteggio dei genitori suddivisi per gruppi di età di esordio."""
    group_name: str
    count: int