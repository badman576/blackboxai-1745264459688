import logging
import importlib
import os

class PluginManager:
    """Manages plugins for the AI system."""
    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self.plugins = []

    def load_plugins(self):
        """Load all plugins from the plugins directory."""
        plugins_dir = os.path.join(os.path.dirname(__file__), '..', 'plugins')
        for filename in os.listdir(plugins_dir):
            if filename.endswith('.py') and filename != '__init__.py':
                module_name = filename[:-3]
                try:
                    module = importlib.import_module(f'plugins.{module_name}')
                    if hasattr(module, 'ExamplePlugin'):
                        plugin_class = getattr(module, 'ExamplePlugin')
                        plugin_instance = plugin_class()
                        self.plugins.append(plugin_instance)
                        self.logger.info(f"Loaded plugin: {module_name}")
                except Exception as e:
                    self.logger.error(f"Failed to load plugin {module_name}: {e}")
        self.logger.info("All plugins loaded")

    def run_plugins(self):
        """Run all loaded plugins."""
        for plugin in self.plugins:
            if hasattr(plugin, 'run'):
                plugin.run()
