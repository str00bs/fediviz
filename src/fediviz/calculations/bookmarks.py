"""File contains bookmarks class, used for extracting & loading data from bookmarks.json"""
from utils import StorageUtil


class Bookmarks:
    """This class loads, transforms and displays bookmarks data"""

    contents: dict

    def __init__(self):
        self.contents = StorageUtil.get_file("bookmarks.json")
