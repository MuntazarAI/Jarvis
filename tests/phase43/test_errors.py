from jarvis.core.errors.handler import ErrorHandler

def test_handle_error():
    handler = ErrorHandler()
    handler.register_handler("ValueError", lambda e: {"handled": True})
    result = handler.handle("ValueError", ValueError("test"))
    assert result["handled"]

def test_error_history():
    handler = ErrorHandler()
    handler.handle("TestError", Exception("msg"))
    history = handler.get_error_history()
    assert len(history) > 0
