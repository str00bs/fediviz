"""
File contains StorageUtil used for managing static files and user uploads
"""
from enum import Enum
import json
from typing import List, Optional
from zipfile import ZipFile
import streamlit as st
from config import Config


class StorageMode(str, Enum):
    """Decides whether to load from archive or state"""
    archive = "archive",
    state = "state"


class StorageUtil:
    """Provides methods for accessing static files and user uploads"""

    Mode: StorageMode = StorageMode

    FILE_OPTIONS: List[str] = [
        "actor.json",
        "bookmarks.json",
        "likes.json",
        "outbox.json",
    ]
    IMAGE_OPTIONS: List[str] = [
        "header.jpg",
        "avatar.png",
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
        for state_key in StorageUtil.STATE_OPTIONS:
            st.session_state[state_key] = None

        for file_name in StorageUtil.FILE_OPTIONS:
            st.session_state[f"files.{file_name}"] = None

        for image_name in StorageUtil.IMAGE_OPTIONS:
            st.session_state[f"images.{image_name}"] = None

        st.session_state["toggles.debugging"] = Config.DEBUGGING
        st.session_state["toggles.initialized"] = True

    @staticmethod
    def get_file(name: str, mode: StorageMode = StorageMode.archive) -> dict:
        """Gets JSON datafile from user archive and returns it as a dict"""
        if mode == StorageMode.archive:
            file = ZipFile(st.session_state.uploaded_file).read(name)
            return json.loads(file.decode())
        if mode == StorageMode.state:
            return st.session_state[f"files.{name}"]

    @staticmethod
    def get_image(name: str, mode: StorageMode = StorageMode.archive):
        """Gets image from user archive"""
        if mode == StorageMode.archive:
            archive = ZipFile(st.session_state.uploaded_file).read(name)
            return archive
        if mode == StorageMode.state:
            return st.session_state[f"images.{name}"]

    @staticmethod
    def save_data():
        for file_name in StorageUtil.FILE_OPTIONS:
            st.session_state[f"files.{file_name}"] = StorageUtil.get_file(file_name)

        for image_name in StorageUtil.IMAGE_OPTIONS:
            st.session_state[f"images.{image_name}"] = StorageUtil.get_image(image_name)
