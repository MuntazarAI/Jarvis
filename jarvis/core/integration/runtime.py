"""Unified runtime integration for JARVIS core subsystems."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any

from jarvis.core.observability.tracer import Tracer
from jarvis.core.streaming.stream import StreamManager
from jarvis.core.graphql.resolver import GraphQLSchema
from jarvis.core.websockets.ws import WebSocketServer
from jarvis.core.messagequeue.queue import QueueManager
from jarvis.core.telemetry.collector import TelemetryCollector
from jarvis.core.middleware.chain import MiddlewareChain
from jarvis.core.typechecking.checker import TypeValidator
from jarvis.core.optimization.optimizer import OptimizationMetrics
from jarvis.core.registry.service_registry import ServiceRegistry
from jarvis.core.errors.handler import ErrorHandler
from jarvis.core.di.container import Container
from jarvis.core.reactive.observable import Observable
from jarvis.core.async_utils.task_manager import AsyncTaskManager
from jarvis.core.batch.processor import BatchProcessor
from jarvis.core.transform.transformer import TransformPipeline
from jarvis.core.statemachine.machine import StateMachine


@dataclass
class JARVISRuntime:
    """Owns and coordinates JARVIS infrastructure components."""

    tracer: Tracer
    streams: StreamManager
    graphql: GraphQLSchema
    websocket: WebSocketServer
    queues: QueueManager
    telemetry: TelemetryCollector
    middleware: MiddlewareChain
    type_validator: TypeValidator
    optimization: OptimizationMetrics
    registry: ServiceRegistry
    errors: ErrorHandler
    di: Container
    reactive: Observable
    async_tasks: AsyncTaskManager
    batch: BatchProcessor
    transforms: TransformPipeline
    state_machine: StateMachine

    @classmethod
    def create(cls) -> "JARVISRuntime":
        """Create a fully wired runtime with all infrastructure phases."""

        return cls(
            tracer=Tracer(),
            streams=StreamManager(),
            graphql=GraphQLSchema(),
            websocket=WebSocketServer(),
            queues=QueueManager(),
            telemetry=TelemetryCollector(),
            middleware=MiddlewareChain(),
            type_validator=TypeValidator(),
            optimization=OptimizationMetrics(),
            registry=ServiceRegistry(),
            errors=ErrorHandler(),
            di=Container(),
            reactive=Observable(),
            async_tasks=AsyncTaskManager(),
            batch=BatchProcessor(),
            transforms=TransformPipeline(),
            state_machine=StateMachine("ready"),
        )

    def initialize(self) -> None:
        """Initialize cross-component infrastructure."""

        # Runtime lifecycle states.
        self.state_machine.add_state("running")
        self.state_machine.add_state("stopped")
        self.state_machine.add_transition("ready", "running", "start")
        self.state_machine.add_transition("running", "stopped", "stop")

        # Core JARVIS event stream.
        self.streams.create_stream("jarvis.events")
        self.streams.create_stream("jarvis.responses")
        self.streams.create_stream("jarvis.errors")

        # Core queues.
        self.queues.create_queue("jarvis.commands")
        self.queues.create_queue("jarvis.events")

        # Telemetry.
        self.telemetry.create_metric("jarvis.command.duration")
        self.telemetry.create_metric("jarvis.command.count")
        self.telemetry.create_metric("jarvis.errors")

        # Runtime service registry.
        self.registry.register(
            "jarvis-runtime",
            "1.0.0",
            "local://jarvis/runtime",
        )

        # Dependency injection registrations.
        self.di.register("tracer", lambda: self.tracer)
        self.di.register("streams", lambda: self.streams)
        self.di.register("queues", lambda: self.queues)
        self.di.register("telemetry", lambda: self.telemetry)
        self.di.register("errors", lambda: self.errors)
        self.di.register("registry", lambda: self.registry)

        # GraphQL base information.
        self.graphql.add_query_field(
            "status",
            "JARVISStatus",
            lambda _: self.status(),
        )

        # WebSocket event forwarding.
        self.streams.get_stream("jarvis.responses").subscribe(
            lambda event: self.websocket.broadcast(
                {
                    "type": "jarvis.response",
                    "data": event,
                }
            )
        )

    def start(self) -> None:
        """Start the integrated runtime."""

        if self.state_machine.get_current_state() == "ready":
            self.state_machine.trigger("start")

    def stop(self) -> None:
        """Stop the integrated runtime."""

        if self.state_machine.get_current_state() == "running":
            self.state_machine.trigger("stop")

    def emit_event(self, event: Any) -> None:
        """Publish an event through the central event stream."""

        stream = self.streams.get_stream("jarvis.events")
        if stream is not None:
            stream.publish(event)

    def emit_response(self, response: Any) -> None:
        """Publish a response through the central response stream."""

        stream = self.streams.get_stream("jarvis.responses")
        if stream is not None:
            stream.publish(response)

    def record_error(self, error: Exception) -> None:
        """Record an error through the unified error pipeline."""

        self.errors.handle(
            type(error).__name__,
            error,
        )

        telemetry = self.telemetry.get_metric("jarvis.errors")
        self.telemetry.record(
            "jarvis.errors",
            1,
        )

        stream = self.streams.get_stream("jarvis.errors")
        if stream is not None:
            stream.publish(
                {
                    "type": type(error).__name__,
                    "message": str(error),
                }
            )

    def status(self) -> dict[str, Any]:
        """Return integrated runtime status."""

        return {
            "state": self.state_machine.get_current_state(),
            "streams": self.streams.list_streams(),
            "queues": self.queues.list_queues(),
            "services": self.registry.list_services(),
            "di_services": self.di.list_services(),
            "websocket_connections": len(self.websocket.connections),
            "graphql_types": list(self.graphql.types.keys()),
            "middleware": self.middleware.get_chain(),
        }
