"""File contains actor class, used for extracting & loading data from actor.json"""
import html
from utils import StorageUtil, StorageMode
from pandas import DataFrame


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

    def __init__(self, mode: StorageMode = StorageMode.state):
        self.data_file = StorageUtil.get_file(self.FILE_NAME, mode)
        self.mode = mode

        # ? Run extractions
        self.extract_name()
        self.extract_summary()
        self.extract_links()
        self.extract_tags()

    def extract_name(self):
        self.name = self.data_file["name"]

    def extract_summary(self):
        self.summary = self.data_file["summary"]

    def extract_links(self):
        """Extract links from actor.json"""
        self.http_url = self.data_file["url"]

        server, user = self.http_url.split('@')
        server = server.replace('/', '').split('https:')[1]

        self.fedi_url = f"@{user}@{server}"

    def extract_tags(self) -> DataFrame:
        """Extract tags from actor.json"""
        df_tags = {"Tag": [], "Description": []}
        for entry in self.data_file["attachment"]:
            df_tags["Tag"].append(entry["name"])
            df_tags["Description"].append(html.unescape(entry["value"]))

        df = DataFrame(df_tags)
        df.set_index("Tag", inplace=True)
        self.tags = df
