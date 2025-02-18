"""File contains reuseable header component"""

import streamlit as st
from streamlit_extras.stylable_container import stylable_container
from utils import StorageMode, StorageUtil


def show_banner(key: str = "header-container"):
    """Reuseable header component"""
    css = "{overflow: hidden; max-height: 15vh; border-radius: 20px;}"
    with stylable_container(key, css):
        try:  # ? To get the banner
            st.image(StorageUtil.get_image("header", mode=StorageMode.state))
        except FileNotFoundError:
            pass
