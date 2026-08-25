from typing import Dict, Callable

class Plugin:
    def __init__(self, name: str, version: str):
        self.name = name
        self.version = version
        self.hooks = {}
    
    def register_hook(self, hook_name: str, callback: Callable):
        if hook_name not in self.hooks:
            self.hooks[hook_name] = []
        self.hooks[hook_name].append(callback)
    
    def get_hooks(self, hook_name: str):
        return self.hooks.get(hook_name, [])

class PluginManager:
    def __init__(self):
        self.plugins = {}
        self.hooks = {}
    
    def load_plugin(self, plugin: Plugin) -> bool:
        self.plugins[plugin.name] = plugin
        return True
    
    def unload_plugin(self, name: str) -> bool:
        if name in self.plugins:
            del self.plugins[name]
            return True
        return False
    
    def register_hook(self, hook_name: str, callback: Callable):
        if hook_name not in self.hooks:
            self.hooks[hook_name] = []
        self.hooks[hook_name].append(callback)
    
    def execute_hooks(self, hook_name: str, *args, **kwargs):
        results = []
        if hook_name in self.hooks:
            for hook in self.hooks[hook_name]:
                results.append(hook(*args, **kwargs))
        return results
    
    def get_plugins(self) -> Dict:
        return {name: p.version for name, p in self.plugins.items()}

_manager = None

def get_plugin_manager():
    global _manager
    if _manager is None:
        _manager = PluginManager()
    return _manager
