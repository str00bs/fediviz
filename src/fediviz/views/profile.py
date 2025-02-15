"""File contains profile page"""

import streamlit as st
from calculations import Actor
from components import show_header
from streamlit_extras.stylable_container import stylable_container
from utils import StorageMode, StorageUtil


class ProfilePage:
    """
    Shows the user their profile page based on uploaded data
    ! This page can only be displayed after a valid archive is uploaded
    """

    actor: Actor

    def __init__(self):
        """When class is called, the page is displayed"""
        self.actor = Actor(StorageMode.state)
        st.header(":material/account_circle: Profile", divider=True)
        show_header(key="profile.header-container")

        left_column, right_column = st.columns(2)

        with left_column:
            try:  # ? To get the avatar
                with stylable_container(
                    "profile.avatar-container",
                    "img {border-radius: 50%; width: 20vw; margin-top: 50px;}",
                ):
                    st.image(StorageUtil.get_image("avatar", mode=StorageMode.state))
            except FileNotFoundError:
                pass

        with right_column:
            st.html(f"<h1>{self.actor.name}</h1>")
            st.table(self.actor.tags)

            nested_left_col, nested_right_col = st.columns(2)

            if st.session_state["toggles.has_followers"]:
                with nested_left_col:
                    st.metric("Followers", st.session_state["user.followers_count"])
                with nested_right_col:
                    st.metric("Follwing", st.session_state["user.following_count"])
            else:
                st.text("No followers/follows loaded")

            st.link_button(
                label=f"Profile: {self.actor.fedi_url}",
                url=self.actor.http_url,
                help="Click open profile on-instance",
                type="primary",
            )

        st.header("Summary", divider=True)

        st.html(self.actor.summary)


ProfilePage()
