"""File contains posts page"""
from utils import StorageMode
from calculations import Outbox
import streamlit as st


class PostsPage:
    """
    Shows the user their posts page based on uploaded data
    ! This page can only be displayed after a valid archive is uploaded
    """

    posts: Outbox

    def __init__(self):
        """When class is called, the page is displayed"""
        self.posts = Outbox(StorageMode.state)
        st.header("Your Posts")


PostsPage()
