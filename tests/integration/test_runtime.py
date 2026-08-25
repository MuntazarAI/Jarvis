from jarvis.core.final.engine import JARVISEngine


def test_engine_wires_core_components():
    engine = JARVISEngine()

    engine.init()

    expected = {
        "runtime",
        "observability",
        "streaming",
        "graphql",
        "websockets",
        "message_queue",
        "telemetry",
        "middleware",
        "typechecking",
        "optimization",
        "service_registry",
        "error_handler",
        "dependency_injection",
        "reactive",
        "async_tasks",
        "batch_processing",
        "transformation",
        "state_machine",
    }

    assert expected.issubset(engine.components.keys())


def test_engine_runtime_initializes():
    engine = JARVISEngine()

    engine.init()

    runtime = engine.get_component("runtime")

    assert runtime is not None
    assert "jarvis.events" in runtime.streams.list_streams()
    assert "jarvis.responses" in runtime.streams.list_streams()
    assert "jarvis.commands" in runtime.queues.list_queues()


def test_engine_start():
    engine = JARVISEngine()

    assert engine.start()
    assert engine.status == "running"
    assert engine.runtime is not None
    assert engine.runtime.state_machine.get_current_state() == "running"


def test_engine_stop():
    engine = JARVISEngine()

    engine.start()
    engine.stop()

    assert engine.status == "stopped"
    assert engine.runtime is not None
    assert engine.runtime.state_machine.get_current_state() == "stopped"


def test_event_to_response_pipeline():
    engine = JARVISEngine()
    engine.start()

    runtime = engine.runtime
    assert runtime is not None

    received = []
    runtime.streams.get_stream("jarvis.responses").subscribe(
        lambda event: received.append(event)
    )

    runtime.emit_response({"text": "Hello"})

    assert received == [{"text": "Hello"}]


def test_websocket_response_bridge():
    engine = JARVISEngine()
    engine.start()

    runtime = engine.runtime
    assert runtime is not None

    connection = runtime.websocket.connect("test-client")

    runtime.emit_response({"text": "Hello from JARVIS"})

    messages = connection.get_messages()

    assert len(messages) == 1
    assert messages[0]["type"] == "jarvis.response"
    assert messages[0]["data"]["text"] == "Hello from JARVIS"


def test_error_pipeline():
    engine = JARVISEngine()
    engine.init()

    runtime = engine.runtime
    assert runtime is not None

    runtime.record_error(ValueError("integration test"))

    history = runtime.errors.get_error_history()

    assert len(history) == 1
    assert history[0]["type"] == "ValueError"
