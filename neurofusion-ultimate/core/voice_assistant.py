import pyttsx3
import logging

class VoiceAssistant:
    """Provides voice capabilities to the AI system."""
    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self.engine = pyttsx3.init()
        self.engine.setProperty('rate', 150)  # Speech rate

    def speak(self, text):
        """Speak the given text."""
        self.logger.info(f"Speaking: {text}")
        self.engine.say(text)
        self.engine.runAndWait()
