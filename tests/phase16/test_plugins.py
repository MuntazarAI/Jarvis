import pytest
from jarvis.core.plugins.manager import get_plugin_manager, Plugin

def test_load_plugin():
    manager = get_plugin_manager()
    plugin = Plugin("test_plugin", "1.0")
    assert manager.load_plugin(plugin)

def test_unload_plugin():
    manager = get_plugin_manager()
    plugin = Plugin("test_remove", "1.0")
    manager.load_plugin(plugin)
    assert manager.unload_plugin("test_remove")

def test_register_hook():
    manager = get_plugin_manager()
    def hook():
        return "hooked"
    manager.register_hook("test_hook", hook)
    results = manager.execute_hooks("test_hook")
    assert len(results) > 0

def test_get_plugins():
    manager = get_plugin_manager()
    plugin = Plugin("p1", "1.5")
    manager.load_plugin(plugin)
    plugins = manager.get_plugins()
    assert "p1" in plugins
