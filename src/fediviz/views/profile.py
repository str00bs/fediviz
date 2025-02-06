"""File contains Profile page"""
import streamlit as st
from utils import StorageUtil
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
        self.actor = Actor()
        st.header(self.actor.name, divider=True)

        with stylable_container("header_container", "{overflow: hidden; max-height: 15vh;}"):
            st.image(StorageUtil.get_image("header.jpg", mode="state"))

        left_column, right_column = st.columns(2)

        with left_column:
            st.image(StorageUtil.get_image("avatar.png", mode="state"))
        with right_column:
            st.table(self.actor.tags)

            nested_left_col, nested_right_col = st.columns(2)

            with nested_left_col:
                st.metric("Followers", 5)
            with nested_right_col:
                st.metric("Follwing", 4)
            st.link_button(
                label=f"Profile: {self.actor.fedi_url}",
                url=self.actor.http_url,
                help="Click open profile on-instance",
                type="primary"
            )

        st.header("Summary", divider=True)
        st.html(self.actor.summary)


ProfilePage()
