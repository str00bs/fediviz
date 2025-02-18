"""File contains reuseable footer component"""

import streamlit as st
from streamlit_extras.bottom_container import bottom
from streamlit_extras.mention import mention

css = """
    <style>
        div[data-testid="stBottom"] .stMarkdown {
            background-color: transparent;
            padding: 0;
            text-align: center;
        }
    </style>
"""


def show_footer():
    """Reuseable footer component"""
    with bottom():
        st.markdown(css, True)  # ? Removes padding added by above components
        mention(
            label="github.com/str00bs/fediviz",
            icon="github",
            url="https://github.com/str00bs/fediviz",
        )
