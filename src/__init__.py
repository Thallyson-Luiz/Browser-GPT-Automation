"""
Browser GPT Automation - Automação do ChatGPT com perfil do Chrome sincronizado.
"""

__version__ = "1.0.0"
__author__ = "Thallyson Luiz"

from .driver_manager import DriverManager
from .chatgpt_automation import ChatGPTAutomation
from .config import Config

__all__ = ["DriverManager", "ChatGPTAutomation", "Config"]
