"""File contains reuseable docs component"""

import streamlit as st

css = """
    <style>
        div[data-testid="stMarkdown"] {
            background-color: #292938;
            padding: 20px;
            border-radius: 20px;
        }
        div[data-testid="stMarkdown"] a {
            text-decoration: none;
        }
    </style>
"""


def show_docs():
    """Reuseable docs component"""
    st.markdown(css + st.session_state["files.README.md"], unsafe_allow_html=True)
