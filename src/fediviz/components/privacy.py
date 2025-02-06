"""File contains reuseable privacy component"""
import streamlit as st
from config import Config


def show_privacy():
    """Reuseable privacy component"""
    st.markdown(st.session_state["files.PRIVACY.md"])
