"""File contains class for Layout management"""
from typing import Sequence
import streamlit as st
from streamlit_extras.bottom_container import bottom
from streamlit_extras.mention import mention

from utils import Uploads
from components import Actor, Bookmarks, Likes, Outbox
from config import Config


class Layout:
    """Manages application layout"""

    tab_labels: Sequence[str] = ["Actor", "Bookmarks", "Likes", "Outbox"]
    tabs: dict = {}

    def __init__(self):
        st.set_page_config(
            page_title="FediViz",
            page_icon=Config.FAVICON
        )
        st.logo(Config.LOGO, size="large")
        self.setup_hero()
        Uploads.show()
        if Uploads.has_file():
            st.snow()
            self.setup_body()

        with bottom():
            self.setup_footer()

    def setup_hero(self):
        """Sets up app hero"""
        st.title("FediViz")

    def setup_body(self):
        """Sets up app body"""
        with st.container():
            self.setup_tabs()
            with self.tabs["Actor"]:
                Actor()
            with self.tabs["Bookmarks"]:
                Bookmarks()
            with self.tabs["Likes"]:
                Likes()
            with self.tabs["Outbox"]:
                Outbox()

    def setup_tabs(self):
        """Sets up app tabs"""
        self.tabs = dict(zip(self.tab_labels, st.tabs(self.tab_labels)))

    def setup_footer(self):
        """Sets up app footer"""
        mention(
            label="github.com/str00bs/fediviz",
            icon="github",
            url="https://github.com/str00bs/fediviz",
        )
