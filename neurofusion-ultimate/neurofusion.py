import logging

from core.secure_system import SecureSystem
from core.self_healing import SelfHealing
from core.autonomous_internet import AutonomousInternet
from core.plugin_manager import PluginManager
from core.gui import GUI
from core.cli import CLI
from core.command_processor import CommandProcessor
from core.anomaly_detection import AnomalyDetection

class NeuroFusionUltimate:
    """Unified AI system entity for NeuroFusion Ultimate."""
    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self.secure_system = SecureSystem()
        self.self_healing = SelfHealing()
        self.autonomous_internet = AutonomousInternet()
        self.plugin_manager = PluginManager()
        self.gui = GUI()
        self.cli = CLI()
        self.command_processor = CommandProcessor()
        self.anomaly_detection = AnomalyDetection()
        self.avatar = None
        self.plugin_manager.load_plugins()

    def set_avatar(self, avatar_url):
        """Set a cool avatar for the AI system."""
        self.avatar = avatar_url
        self.logger.info(f"Avatar set to: {avatar_url}")

    def get_avatar(self):
        """Get the current avatar URL."""
        return self.avatar

    def initialize(self):
        """Initialize all core components."""
        self.logger.info("Initializing NeuroFusion Ultimate AI system...")
        self.secure_system.initialize()
        self.self_healing.initialize()
        self.autonomous_internet.initialize()
        self.logger.info("Initialization complete.")

    def start(self):
        """Start all core components."""
        self.logger.info("Starting NeuroFusion Ultimate AI system...")
        self.gui.start()
        self.cli.start()
        self.command_processor.start()
        self.anomaly_detection.monitor()
        self.logger.info("NeuroFusion Ultimate AI system started.")
