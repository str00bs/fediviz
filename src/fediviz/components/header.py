"""File contains reuseable header component"""

import streamlit as st
from streamlit_extras.stylable_container import stylable_container
from utils import StorageMode, StorageUtil


def show_header(key: str = "header-container"):
    """Reuseable header component"""
    css = "{overflow: hidden; max-height: 15vh; border-radius: 20px;}"
    with stylable_container(key, css):
        try:
            st.image(StorageUtil.get_image("header", mode=StorageMode.state))
        except FileNotFoundError:
            pass
