"""File contains bookmarks class, used for extracting & loading data from bookmarks.json"""
from utils import StorageUtil, StorageMode


class Bookmarks:
    """This class is used to extract & transform bookmarks data"""

    # ? Static properties
    FILE_NAME: str = "bookmarks.json"
    data_file: dict
    mode: StorageMode

    def __init__(self, mode: StorageMode = StorageMode.state):
        self.data_file = StorageUtil.get_file(self.FILE_NAME, mode)
        self.mode = mode
