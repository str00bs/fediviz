"""File contains likes page"""
from utils import StorageMode
from calculations import Likes
import streamlit as st


class LikesPage:
    """
    Shows the user their likes page based on uploaded data
    ! This page can only be displayed after a valid archive is uploaded
    """

    likes: Likes

    def __init__(self):
        """When class is called, the page is displayed"""
        self.likes = Likes(StorageMode.state)
        st.header("Your Likes")


LikesPage()
