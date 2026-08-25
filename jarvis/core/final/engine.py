"""Main JARVIS application engine."""

from __future__ import annotations

from typing import Any

from jarvis.core.integration.runtime import JARVISRuntime


class JARVISEngine:
    """Top-level JARVIS lifecycle and infrastructure coordinator."""

    def __init__(self) -> None:
        self.initialized = False
        self.components: dict[str, Any] = {}
        self.status = "stopped"
        self.runtime: JARVISRuntime | None = None

    def init(self) -> None:
        """Initialize every integrated JARVIS subsystem."""

        if self.initialized:
            return

        self.runtime = JARVISRuntime.create()
        self.runtime.initialize()

        self._register_runtime_components()

        self.initialized = True
        self.status = "initialized"

    def _register_runtime_components(self) -> None:
        """Expose integrated infrastructure through the main engine."""

        if self.runtime is None:
            raise RuntimeError("Runtime has not been created")

        self.register_component("runtime", self.runtime)
        self.register_component("observability", self.runtime.tracer)
        self.register_component("streaming", self.runtime.streams)
        self.register_component("graphql", self.runtime.graphql)
        self.register_component("websockets", self.runtime.websocket)
        self.register_component("message_queue", self.runtime.queues)
        self.register_component("telemetry", self.runtime.telemetry)
        self.register_component("middleware", self.runtime.middleware)
        self.register_component("typechecking", self.runtime.type_validator)
        self.register_component("optimization", self.runtime.optimization)
        self.register_component("service_registry", self.runtime.registry)
        self.register_component("error_handler", self.runtime.errors)
        self.register_component("dependency_injection", self.runtime.di)
        self.register_component("reactive", self.runtime.reactive)
        self.register_component("async_tasks", self.runtime.async_tasks)
        self.register_component("batch_processing", self.runtime.batch)
        self.register_component("transformation", self.runtime.transforms)
        self.register_component("state_machine", self.runtime.state_machine)

    def start(self) -> bool:
        """Start JARVIS."""

        if not self.initialized:
            self.init()

        if self.runtime is None:
            return False

        self.runtime.start()
        self.status = "running"

        self.runtime.emit_event(
            {
                "type": "engine.started",
                "status": self.status,
            }
        )

        return True

    def stop(self) -> bool:
        """Stop JARVIS."""

        if self.runtime is not None:
            self.runtime.stop()
            self.runtime.emit_event(
                {
                    "type": "engine.stopped",
                    "status": "stopped",
                }
            )

        self.status = "stopped"
        return True

    def register_component(self, name: str, component: Any) -> None:
        """Register an application component."""

        self.components[name] = component

    def get_component(self, name: str) -> Any:
        """Retrieve a registered component."""

        return self.components.get(name)

    def get_status(self) -> dict[str, Any]:
        """Return complete JARVIS engine status."""

        result = {
            "status": self.status,
            "initialized": self.initialized,
            "components": len(self.components),
        }

        if self.runtime is not None:
            result["runtime"] = self.runtime.status()

        return result


_engine: JARVISEngine | None = None


def get_jarvis_engine() -> JARVISEngine:
    """Return the process-wide JARVIS engine."""

    global _engine

    if _engine is None:
        _engine = JARVISEngine()

    return _engine
