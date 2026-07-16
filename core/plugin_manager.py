import os
import importlib


class PluginManager:

    def __init__(self):

        self.plugins = {}

    def load_plugins(self):

        folder = "plugins"

        for filename in os.listdir(folder):

            if (
                filename.endswith(".py")
                and filename != "__init__.py"
            ):

                module = importlib.import_module(
                    f"plugins.{filename[:-3]}"
                )

                if hasattr(module, "register"):

                    module.register(self)

    def register(self, name, func):

        self.plugins[name] = func

    def execute(self, name, *args):

        if name not in self.plugins:
            return None

        return self.plugins[name](*args)

    def list_plugins(self):

        return sorted(self.plugins.keys())


plugin_manager = PluginManager()