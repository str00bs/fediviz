"""File contains profile page"""
import streamlit as st
from utils import StorageUtil, StorageMode
from streamlit_extras.stylable_container import stylable_container
from calculations import Actor


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
        with stylable_container("header_container", "{overflow: hidden; max-height: 15vh;}"):
            st.image(StorageUtil.get_image("header.jpg", mode="state"))

        left_column, right_column = st.columns(2)

        with left_column:
            st.html("")
            st.html("")
            st.image(StorageUtil.get_image("avatar.png", mode="state"))
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
                type="primary"
            )

        st.header("Summary", divider=True)

        st.html(self.actor.summary)



ProfilePage()
