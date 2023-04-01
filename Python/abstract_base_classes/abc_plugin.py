"""ABCs are a great way to write a baseline plugin interface"""

import abc


class ServicePlugin(metaclass=abc.ABCMeta):

    plugins = {}

    def __new__(cls, *args, **kwargs):
        """Add singleton pattern to plugin classes"""
        if cls not in cls.plugins:
            cls.plugins[cls] = super().__new__(cls)
        return cls.plugins[cls]

    def __init__(self):
        print(f"Initializing {self.__class__.__name__}...")

    @classmethod
    def register(cls, plugin):
        print(f"Registering {plugin.__name__}...")
        if issubclass(plugin, cls):
            plugin()
        elif all([hasattr(plugin, method) for method in ["start", "stop", "status"]]):
            # register the plugin as a subclass of ServicePlugin
            abc.ABCMeta.register(cls, plugin)
            cls.plugins[plugin] = plugin()
        else:
            raise TypeError("Plugins must define start, stop, and status methods")

    @abc.abstractclassmethod
    def start(self):
        pass

    @abc.abstractclassmethod
    def stop(self):
        pass

    @abc.abstractclassmethod
    def status(self):
        pass

    @classmethod
    def start_all(cls):
        for plugin in list(cls.plugins.values()):
            plugin.start()

    @classmethod
    def stop_all(cls):
        for plugin in list(cls.plugins.values()):
            plugin.stop()


class MyPlugin(ServicePlugin):

    def start(self):
        print("Starting MyPlugin...")

    def stop(self):
        print("Stopping MyPlugin...")

    def status(self):
        print("MyPlugin status!")


class AnotherPlugin:

    def start(self):
        print("Starting AnotherPlugin...")

    def stop(self):
        print("Stopping AnotherPlugin...")

    def status(self):
        print("AnotherPlugin status!")
