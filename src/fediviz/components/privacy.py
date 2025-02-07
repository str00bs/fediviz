"""File contains reuseable privacy component"""

import streamlit as st


def show_privacy():
    """Reuseable privacy component"""
    st.markdown(st.session_state["files.PRIVACY.md"])
