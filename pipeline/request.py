from dataclasses import dataclass
from pathlib import Path


@dataclass(slots=True)
class EngineeringRequest:
    """
    Represents one engineering task.

    Everything required to complete a repair
    is stored here.
    """

    goal: str

    root: Path = Path(".")

    mode: str = "repair"

    model: str | None = None

    max_iterations: int = 3

    dry_run: bool = False