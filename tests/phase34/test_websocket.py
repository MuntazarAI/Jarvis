import pytest
from jarvis.core.websockets.ws import WebSocketServer

def test_connect():
    server = WebSocketServer()
    conn = server.connect("c1")
    assert conn.is_open

def test_send_message():
    server = WebSocketServer()
    conn = server.connect("c2")
    conn.send({"msg": "hello"})
    messages = conn.get_messages()
    assert len(messages) > 0

def test_broadcast():
    server = WebSocketServer()
    server.connect("c3")
    server.broadcast({"broadcast": "msg"})
    for conn in server.connections.values():
        assert len(conn.get_messages()) > 0
