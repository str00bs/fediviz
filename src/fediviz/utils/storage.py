"""
File contains StorageUtil used for managing static files and user uploads
"""
import json
from typing import List, Optional
from zipfile import ZipFile
import streamlit as st
from config import Config


class StorageUtil:
    """Provides methods for accessing static files and user uploads"""
    FILE_OPTIONS: List[str] = [
        "actor.json",
        "bookmarks.json",
        "likes.json",
        "outbox.json",
    ]
    STATE_OPTIONS: List[str] = {
        # ? Toggles
        "toggles.initialized",
        "toggles.debugging",
        "toggles.has_completed_steps",
        "toggles.has_followers",
        # ? Pages
        "welcome.user_url",
    }

    @staticmethod
    def init_state():
        """Initializes global app state"""
        for state in StorageUtil.STATE_OPTIONS:
            st.session_state[state] = None

        for filepath in StorageUtil.FILE_OPTIONS:
            st.session_state[f"files.{filepath}"] = None

        st.session_state["toggles.debugging"] = Config.DEBUGGING
        st.session_state["toggles.initialized"] = True

    @staticmethod
    def get_file(name: str) -> dict:
        """Gets JSON datafile from user archive and returns it as a dict"""
        file = ZipFile(st.session_state.uploaded_file).read(name)
        return json.loads(file.decode())

    @staticmethod
    def get_state_file(name: str) -> dict:
        """Gets datafile from state and returns it as a dict"""
        return st.session_state[f"files.{name}"]

    @staticmethod
    def get_image(name: str):
        """Gets image from user archive"""
        archive = ZipFile(st.session_state.uploaded_file).read(name)
        return archive

    @staticmethod
    def save_data():
        for filepath in StorageUtil.FILE_OPTIONS:
            st.session_state[f"files.{filepath}"] = StorageUtil.get_file(filepath)
