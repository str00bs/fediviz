"""File contains reuseable license component"""
import streamlit as st
from config import Config


def show_license():
    """Reuseable license component"""
    st.markdown(st.session_state["files.LICENSE.md"])
