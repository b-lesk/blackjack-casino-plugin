from abc import ABC, abstractmethod

class PluginInterface(ABC):
    @abstractmethod
    def initialize(self):
        pass

    @abstractmethod
    def display_advice(self, advice):
        pass

    @abstractmethod
    def handle_user_interaction(self):
        pass

    @abstractmethod
    def set_hotkey(self, key):
        pass

    @abstractmethod
    def voice_alert(self, message):
        pass