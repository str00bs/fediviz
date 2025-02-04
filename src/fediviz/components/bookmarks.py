"""
File contains bookmarks class, used for:
- Loading
- Transforming
- Displaying

bookmarks data from the users upload.
"""
import streamlit as st
from utils import Uploads


class Bookmarks:
    """This class loads, transforms and displays bookmarks data"""

    contents: dict

    def __init__(self):
        self.contents = Uploads.get_file("bookmarks.json")
