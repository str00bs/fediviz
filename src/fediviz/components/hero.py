"""File contains reuseable hero component"""

import streamlit as st
from config import Config


def show_hero():
    """Reuseable hero component"""
    st.logo(Config.LOGO, size="large")
    st.title("Fedi Vizualizer", help="`FediViz` for short")
    if st.session_state["toggles.debugging"]:
        with st.expander("State (Debugging: True)"):
            sorted_json = {k: st.session_state[k] for k in sorted(st.session_state)}
            st.json(sorted_json, expanded=False)
