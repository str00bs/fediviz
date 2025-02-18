"""File contains reuseable license component"""

import streamlit as st

css_component = """
    <style>
        div[data-testid="stMarkdown"] {
            background-color: #292938;
            padding: 20px;
            border-radius: 20px;
        }
    </style>
"""


def show_license():
    """Reuseable license component"""

    st.markdown(
        css_component + st.session_state["files.LICENSE.md"], unsafe_allow_html=True
    )
