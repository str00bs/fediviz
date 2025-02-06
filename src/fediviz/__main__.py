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


if __name__ == "__main__":
    # ? Set global streamlit configuration
    st.set_page_config(
        page_title="FediViz",
        page_icon=Config.FAVICON
    )

    # ? Initialize global state
    if "toggles.initialized" not in st.session_state:
        StorageUtil.init_state()

    # ? Define Views
    welcome_views = {
        "App": [
            st.Page("views/welcome.py", title="Welcome", default=True),
        ],
        "Resources": [
            st.Page("views/license.py", title="License", url_path="license"),
            st.Page("views/privacy.py", title="Privacy", url_path="privacy")
        ]
    }

    data_views = {
        "App": [
            st.Page("views/profile.py", title="Profile", url_path="profile", icon=":material/person:"),
            st.Page("views/bookmarks.py", title="Bookmarks", url_path="bookmarks", icon=":material/bookmark:"),
            st.Page("views/likes.py", title="Likes", url_path="likes", icon=":material/thumb_up:"),
            st.Page("views/posts.py", title="Posts", url_path="posts", icon=":material/docs:"),
        ],
        "Resources": [
            st.Page("views/license.py", title="License", url_path="license", icon=":material/license:"),
            st.Page("views/privacy.py", title="Privacy", url_path="privacy", icon=":material/visibility_off:"),
        ]
    }

    # ? Call global components
    show_hero()
    show_footer()

    # ? Decide on which views to display
    if st.session_state["toggles.has_completed_steps"]:
        app = st.navigation(pages=data_views, expanded=True)
    else:
        app = st.navigation(pages=welcome_views, expanded=True)

    # ? Run application
    app.run()
