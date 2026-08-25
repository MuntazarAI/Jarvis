"""
Standard runtime result object.

Every runtime tool in Jarvis should return a RuntimeResult.
"""

from dataclasses import dataclass, field
from typing import Any


@dataclass(slots=True)
class RuntimeResult:
    """
    Standard return value for every runtime tool.
    """

    success: bool
    action: str

    data: Any = None

    error: str | None = None

    metadata: dict = field(default_factory=dict)

    @classmethod
    def ok(
        cls,
        action: str,
        data: Any = None,
        **metadata,
    ):
        return cls(
            success=True,
            action=action,
            data=data,
            error=None,
            metadata=metadata,
        )

    @classmethod
    def fail(
        cls,
        action: str,
        error: str,
        data: Any = None,
        **metadata,
    ):
        return cls(
            success=False,
            action=action,
            data=data,
            error=error,
            metadata=metadata,
        )

    def to_dict(self):

        return {
            "success": self.success,
            "action": self.action,
            "data": self.data,
            "error": self.error,
            "metadata": self.metadata,
        }

    def __bool__(self):
        return self.success

    def __repr__(self):
        return (
            f"RuntimeResult("
            f"success={self.success}, "
            f"action={self.action!r})"
        )