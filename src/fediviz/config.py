"""File contains app config"""

from os import getenv
from pathlib import Path
from typing import Union

from pydantic import Field, HttpUrl
from pydantic_settings import BaseSettings, SettingsConfigDict


class appConfig(BaseSettings):
    """Contains config for the App itself"""

    model_config = SettingsConfigDict(env_prefix="APP_")

    # ? General
    REPO_URL: HttpUrl = Field("https://github.com/str00bs/fediviz")
    STATIC_DIR: Path = Field("fediviz/static")

    # ? Images
    FAVICON: Union[Path, str] = Field("strawberry.png")
    LOGO: Union[Path, str] = Field("strawberry.png")
    AVATAR: Union[Path, str] = Field("defaults/avatar.png")
    GITHUB_LOGO: Union[Path, str] = Field("github.png")
    MASTODON_LOGO: Union[Path, str] = Field("mastodon.png")

    # ? Files
    LICENSE: Union[Path, str] = Field("LICENSE.md")
    PRIVACY: Union[Path, str] = Field("PRIVACY.md")
    DOCS: Union[Path, str] = Field("README.md")

    def __init__(self):
        """Sets relative path for each static variable"""
        super(appConfig, self).__init__()

        # ? Images
        self.FAVICON = self.STATIC_DIR.joinpath(self.FAVICON)
        self.LOGO = self.STATIC_DIR.joinpath(self.LOGO)
        self.AVATAR = self.STATIC_DIR.joinpath(self.AVATAR)
        self.GITHUB_LOGO = self.STATIC_DIR.joinpath(self.GITHUB_LOGO)
        self.MASTODON_LOGO = self.STATIC_DIR.joinpath(self.MASTODON_LOGO)

        # ? Files
        self.LICENSE = self.STATIC_DIR.joinpath(self.LICENSE)
        self.PRIVACY = self.STATIC_DIR.joinpath(self.PRIVACY)
        self.DOCS = self.STATIC_DIR.joinpath(self.DOCS)


class stConfig(BaseSettings):
    """Contains config for Streamlit"""

    model_config = SettingsConfigDict(env_prefix="STREAMLIT_")

    # ? Global variables
    STREAMLIT_GLOBAL_DEVELOPMENT_MODE: bool = False

    # ? Server variables
    STREAMLIT_SERVER_HOST: str = Field("localhost")
    STREAMLIT_SERVER_PORT: int = Field(80)
    STREAMLIT_SERVER_MAX_UPLOAD_SIZE: int = Field(1000)
    STREAMLIT_SERVER_ENABLE_STATIC_SERVING: bool = Field(True)

    # ? Browser variables
    STREAMLIT_BROWSER_SERVER_ADDRESS: str = Field("localhost")
    STREAMLIT_BROWSER_SERVER_PORT: int = Field(80)
    STREAMLIT_BROWSER_GATHER_USAGE_STATS: bool = Field(False)

    # ? Theme variables
    STREAMLIT_THEME_BASE: str = Field("dark")
    STREAMLIT_THEME_PRIMARY_COLOR: str = Field("#5c49e1")
    STREAMLIT_THEME_BACKGROUND_COLOR: str = Field("#0E1117")
    STREAMLIT_THEME_SECONDARY_BACKGROUND_COLOR: str = Field("#373e75")
    STREAMLIT_THEME_TEXT_COLOR: str = Field("#FAFAFA")


Config = appConfig()
STConfig = stConfig()
