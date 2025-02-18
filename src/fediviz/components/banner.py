"""File contains reuseable header component"""

import streamlit as st
from streamlit_extras.stylable_container import stylable_container
from utils import StorageMode, StorageUtil

css = """
    [data-testid="stImageContainer"] {
        overflow: hidden;
        max-height: 15vh;
        border-radius: 20px;
    }
"""


def show_banner(key: str = "header-container"):
    """Reuseable header component"""

    with stylable_container(key, css):
        try:  # ? To get the banner
            st.image(StorageUtil.get_image("header", mode=StorageMode.state))
        except FileNotFoundError:
            pass
