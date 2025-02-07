"""File contains app config"""
from pathlib import Path
from os import getenv, environ
from dotenv import load_dotenv


class _config:
    """Contains app config"""
    # ? Images
    STATIC_DIR: Path
    FAVICON: Path
    LOGO: Path
    GITHUB_LOGO: Path
    MASTODON_LOGO: Path

    # ? Links
    GITHUB_URL: Path

    # ? Files
    LICENSE: str
    PRIVACY: str

    def __init__(self):
        load_dotenv()

        # ? Images
        self.STATIC_DIR = Path(getenv("STATIC_DIR"))
        self.FAVICON = self.STATIC_DIR.joinpath(getenv('FAVICON'))
        self.LOGO = self.STATIC_DIR.joinpath(getenv('LOGO'))
        self.GITHUB_LOGO = self.STATIC_DIR.joinpath(getenv('GITHUB_LOGO'))
        self.MASTODON_LOGO = self.STATIC_DIR.joinpath(getenv('MASTODON_LOGO'))

        # ? Links
        self.GITHUB_URL = getenv("GITHUB_URL")

        # ? Toggles
        self.DEBUGGING = getenv("DEBUGGING")

        # ? Files
        self.LICENSE = self.STATIC_DIR.joinpath(getenv("LICENSE"))
        self.PRIVACY = self.STATIC_DIR.joinpath(getenv("PRIVACY"))
        self.DOCS = self.STATIC_DIR.joinpath(getenv("README"))


Config = _config()
