"""File contains class for Layout management"""
from typing import Sequence

import streamlit as st
from streamlit_extras.app_logo import add_logo
from streamlit_extras.bottom_container import bottom

from utils import Uploads
from components.outbox import Outbox
from config import Config


class Layout:
    """Manages application layout"""

    uploads_container: object

    def __init__(self):
        st.set_page_config(
            layout="wide",
            page_title="FediViz",
            page_icon=Config.FAVICON
        )

        if not Uploads.has_file():
            Uploads.show()

        if Uploads.has_file():
            with st.container():
                Outbox()

        with bottom():
            self.setup_footer()

    def setup_hero(self):
        """Sets up app hero"""
        st.title("FediViz")
        st.logo(Config.FAVICON, size="large")
        # TODO: GitHub Link

    def setup_nav(self):
        """Sets up app nav"""
        # ? Sidebar, tabs or tab-bar?
        raise NotImplementedError

    def setup_footer(self):
        """Sets up app footer"""
        # TODO: Fully implement
        st.text("Footer")
        # TODO: Coffee link
