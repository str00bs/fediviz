"""
File contains layout class, used for:
- Loading
- Transforming
- Displaying

layout data from the users upload.
"""
from typing import Sequence

import streamlit as st


class Layout:
    """This class loads, transforms and displays layout data"""

    def __init__(self):
        st.set_page_config(layout="wide")
        st.title("FediViz")

    def setup_tabs(tabs: Sequence[str]):
        raise NotImplementedError
