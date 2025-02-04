"""File contains class used for uploading user data"""
import json
from logging import getLogger, Logger
from os import getenv
from pathlib import Path
from typing import Optional


static_dir: Path = getenv("STATIC_DIR")
logger: Logger = getLogger("__name__")


class Uploads:
    """This class manages user data uploads"""

    @staticmethod
    def get(path: Optional[Path] = static_dir) -> dict:
        """Gets user upload from path and returns it as a dictionary"""
        logger.debug(f"Uploads.get(path='{path}')")
        # TODO: Switch to user-upload instead of static data
        with open(static_dir) as fp:
            data = json.load(fp)
            return data
