from dataclasses import dataclass, field


@dataclass(slots=True)
class EngineeringContext:
    """
    Shared state throughout one engineering task.

    Every stage reads from and writes to this object.
    """

    request: object

    project: dict = field(default_factory=dict)

    dependency_graph: dict = field(default_factory=dict)

    affected_files: dict = field(default_factory=dict)

    analysis: dict = field(default_factory=dict)

    plan: dict = field(default_factory=dict)

    patches: list = field(default_factory=list)

    validation: dict = field(default_factory=dict)

    history: list = field(default_factory=list)

    success: bool = False

    error: str | None = None