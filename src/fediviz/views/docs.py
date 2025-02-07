"""File contains Docs page"""
import streamlit as st
from components.docs import show_docs


class DocsPage:
    """Shows the user the app's docs agreement"""

    def __init__(self):
        """When class is called, the page is displayed"""
        with st.container(key="DocsPage.body"):
            show_docs()


DocsPage()
