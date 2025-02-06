"""
Application main file
- Sets up global configuration
- Sets up global components
- Sets up navigation
- Runs the application
"""

from config import Config
from components.footer import show_footer
from components.hero import show_hero
from utils import StorageUtil
import streamlit as st


def debug_switch():
    st.session_state["toggles.debugging"] = not st.session_state["toggles.debugging"]


if __name__ == "__main__":
    # ? Set global streamlit configuration
    st.set_page_config(
        page_title="FediViz",
        page_icon=Config.FAVICON
    )

    # ? Initialize global state
    if "toggles.initialized" not in st.session_state:
        StorageUtil.init_state()
        StorageUtil.load_extras()

    # ? Define Views
    welcome_views = {
        "App": [
            st.Page("views/welcome.py", title="Welcome", default=True, icon=":material/home:"),
        ],
        "Resources": [
            st.Page("views/license.py", title="License", url_path="license", icon=":material/license:"),
            st.Page("views/privacy.py", title="Privacy", url_path="privacy", icon=":material/visibility_off:")
        ]
    }

    data_views = {
        "App": [
            st.Page("views/profile.py", title="Profile", url_path="profile", icon=":material/account_circle:"),
            st.Page("views/bookmarks.py", title="Bookmarks", url_path="bookmarks", icon=":material/bookmarks:"),
            st.Page("views/likes.py", title="Likes", url_path="likes", icon=":material/thumb_up:"),
            st.Page("views/posts.py", title="Posts", url_path="posts", icon=":material/stacked_email:"),
        ],
        "Resources": [
            st.Page("views/license.py", title="License", url_path="license", icon=":material/license:"),
            st.Page("views/privacy.py", title="Privacy", url_path="privacy", icon=":material/visibility_off:"),
        ]
    }

    # ? Call global components
    show_hero()
    show_footer()

    st.session_state["toggles.debugging"] = st.sidebar.toggle(
        label="Debug",
        value=False,
        on_change=debug_switch
    )

    # ? Decide on which views to display
    if st.session_state["toggles.has_completed_steps"]:
        app = st.navigation(pages=data_views, expanded=True)
    else:
        app = st.navigation(pages=welcome_views, expanded=True)

    # ? Run application
    app.run()
