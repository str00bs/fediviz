"""File contains app config"""
from os import getenv


class _config:
    """Contains app config"""
    STATIC_DIR: str
    FAVICON: str
    LOGO: str
    GITHUB_URL: str
    GITHUB_LOGO: str

    def __init__(self):
        self.STATIC_DIR = getenv("STATIC_DIR")
        self.FAVICON = f"{self.STATIC_DIR}/{getenv('FAVICON')}"
        self.LOGO = f"{self.STATIC_DIR}/{getenv('LOGO')}"
        self.GITHUB_URL = getenv("GITHUB_URL")
        self.GITHUB_LOGO = getenv("GITHUB_LOGO")


Config = _config()
