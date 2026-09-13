from .gender import Gender

@dataclass
class Child:
    """
    Represents a child in the domain model.
    """

    family_id: str
    gender: Gender