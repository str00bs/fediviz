"""File contains license page"""

import streamlit as st
from components.license import show_license


class LicensePage:
    """Shows the user the app's license agreement"""

    def __init__(self):
        """When class is called, the page is displayed"""
        with st.container(key="LicensePage.body"):
            show_license()


LicensePage()
