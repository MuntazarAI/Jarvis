from dataclasses import dataclass, field
from typing import Any


@dataclass(slots=True)
class AgentState:
    """
    Represents the current reasoning state of the engineering agent.
    """

    goal: str

    status: str = "thinking"

    current_step: int = 0

    max_steps: int = 100

    finished: bool = False

    success: bool = False

    current_action: str = ""

    observation: str = ""

    thoughts: list[str] = field(default_factory=list)

    actions: list[dict] = field(default_factory=list)

    observations: list[dict] = field(default_factory=list)

    memory: list[dict] = field(default_factory=list)

    files_read: set[str] = field(default_factory=set)

    files_written: set[str] = field(default_factory=set)

    files_modified: set[str] = field(default_factory=set)

    variables: dict[str, Any] = field(default_factory=dict)

    errors: list[str] = field(default_factory=list)

    metadata: dict[str, Any] = field(default_factory=dict)

    last_action: str = ""

    last_args: dict = field(default_factory=dict)

    last_result: dict = field(default_factory=dict)

    def next_step(self):

        self.current_step += 1

    def stop(self, success: bool):

        self.finished = True

        self.success = success

    def add_thought(self, thought: str):

        self.thoughts.append(thought)

    def add_action(self, action: dict):

        self.actions.append(action)

        self.last_action = action.get("action", "")

        self.last_args = action.get("args", {})

    def add_observation(self, observation: dict):

        self.observations.append(observation)

        self.last_result = observation.get("result", {})

    def add_error(self, error: str):

        self.errors.append(error)

    def remember(self, item: dict):

        self.memory.append(item)

    def summary(self):

        return {
            "goal": self.goal,
            "status": self.status,
            "steps": self.current_step,
            "finished": self.finished,
            "success": self.success,
            "thoughts": len(self.thoughts),
            "actions": len(self.actions),
            "observations": len(self.observations),
            "memory": len(self.memory),
            "errors": len(self.errors),
            "files_read": len(self.files_read),
            "files_written": len(self.files_written),
            "files_modified": len(self.files_modified),
        }


agent_state = AgentState