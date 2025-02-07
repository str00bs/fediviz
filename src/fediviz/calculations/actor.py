"""File contains actor class, used for extracting & loading data from actor.json"""

import html
from typing import List

from pandas import DataFrame
from utils import StorageMode, StorageUtil


class Actor:
    """This class is used to extract & transform actor data"""

    # ? Static properties
    FILE_NAME: str = "actor.json"
    data_file: dict
    mode: StorageMode

    # ? Dynamic (data) properties
    name: str
    summary: str
    http_url: str
    fedi_url: str
    tags: dict
    emojis: List[dict]

    def __init__(self, mode: StorageMode = StorageMode.state):
        self.data_file = StorageUtil.get_file(self.FILE_NAME, mode)
        self.mode = mode

        # ? Run extractions
        self.extract_tags()
        self.extract_links()
        self.extract_emoji()
        self.extract_name()
        self.extract_summary()

    def extract_tags(self) -> DataFrame:
        """Extract tags from actor.json"""
        df_tags = {"Tag": [], "Description": []}
        for entry in self.data_file["attachment"]:
            df_tags["Tag"].append(entry["name"])
            df_tags["Description"].append(html.unescape(entry["value"]))

        df = DataFrame(df_tags)
        df.set_index("Tag", inplace=True)
        self.tags = df

    def extract_links(self):
        """Extract links from actor.json"""
        self.http_url = self.data_file["url"]

        server, user = self.http_url.split("@")
        server = server.replace("/", "").split("https:")[1]

        self.fedi_url = f"@{user}@{server}"

    def extract_emoji(self) -> DataFrame:
        """Extract tags from actor.json"""
        emojis = {}
        for entry in self.data_file["tag"]:
            if "icon" in entry:
                emojis.update({entry["name"]: entry["icon"]["url"]})

        self.emojis = emojis

    def inject_emojis(self, string: str) -> str:
        injected_string = string
        for short_code, url in self.emojis.items():
            old = f"{short_code}"
            new = f"<img src='{url}' height='16px' width='16px'>"
            injected_string = injected_string.replace(old, new)

        return injected_string

    def extract_name(self):
        name = self.data_file["name"]
        self.name = self.inject_emojis(name)

    def extract_summary(self):
        summary: str = self.data_file["summary"]
        self.summary = self.inject_emojis(summary)
