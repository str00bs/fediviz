"""File contains reuseable docs component"""

import streamlit as st


def show_docs():
    """Reuseable docs component"""
    st.markdown(st.session_state["files.README.md"])
