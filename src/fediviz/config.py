"""File contains app config"""

from os import getenv
from pathlib import Path

from dotenv import load_dotenv


class _config:
    """Contains app config"""

    # ? General
    REPO_URL: str
    STATIC_DIR: Path

    # ? Images
    FAVICON: Path
    LOGO: Path
    GITHUB_LOGO: Path
    MASTODON_LOGO: Path

    # ? Files
    LICENSE: str
    PRIVACY: str

    def __init__(self):
        load_dotenv()

        # ? General
        self.REPO_URL = getenv("REPO_URL")
        self.STATIC_DIR = Path(getenv("STATIC_DIR"))

        # ? Images
        self.FAVICON = self.STATIC_DIR.joinpath(getenv("FAVICON"))
        self.LOGO = self.STATIC_DIR.joinpath(getenv("LOGO"))
        self.GITHUB_LOGO = self.STATIC_DIR.joinpath("github.png")
        self.MASTODON_LOGO = self.STATIC_DIR.joinpath("mastodon.png")

        # ? Files
        self.LICENSE = self.STATIC_DIR.joinpath("LICENSE.md")
        self.PRIVACY = self.STATIC_DIR.joinpath("PRIVACY.md")
        self.DOCS = self.STATIC_DIR.joinpath("README.md")


Config = _config()
