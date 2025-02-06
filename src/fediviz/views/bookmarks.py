"""File contains bookmarks page"""
from utils import StorageMode
from calculations import Bookmarks
import streamlit as st


class BookmarksPage:
    """
    Shows the user their bookmarks page based on uploaded data
    ! This page can only be displayed after a valid archive is uploaded
    """

    bookmarks: Bookmarks

    def __init__(self):
        """When class is called, the page is displayed"""
        self.bookmarks = Bookmarks(StorageMode.state)
        st.header("Your Bookmarks")


BookmarksPage()
