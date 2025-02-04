"""Root module of the application"""
import importlib.metadata
from config import Config

CONFIG = Config()

__version__ = importlib.metadata.version("fediviz")
__author__ = importlib.metadata.author("fediviz")
