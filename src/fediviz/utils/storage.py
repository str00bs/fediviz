"""
File contains StorageUtil used for managing static files and user uploads
"""

import json
from enum import Enum
from typing import Any, List
from zipfile import ZipFile

import streamlit as st
from config import Config


class StorageMode(str, Enum):
    """Decides whether to load from archive or state"""

    archive = ("archive",)
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
    STATE_OPTIONS: List[str] = [
        # ? Toggles
        "toggles.initialized",
        "toggles.debugging",
        "toggles.has_completed_steps",
        "toggles.has_followers",
        # ? Pages
        "welcome.user_url",
    ]
    USER_OPTIONS: List[str] = [
        "user.id",
        "user.followers_count",
        "user.following_count",
        "user.created_at",
    ]

    @staticmethod
    def init_state():
        """Initializes global app state"""
        for state_key in StorageUtil.STATE_OPTIONS:
            st.session_state[state_key] = None

        for file_name in StorageUtil.FILE_OPTIONS:
            st.session_state[f"files.{file_name}"] = None

        for image_name in StorageUtil.IMAGE_OPTIONS:
            st.session_state[f"images.{image_name}"] = None

        for user_option in StorageUtil.USER_OPTIONS:
            st.session_state[f"user.{user_option}"] = None

        st.session_state["toggles.debugging"] = False
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

    # ? Callbacks
    @staticmethod
    def save_data():
        for file_name in StorageUtil.FILE_OPTIONS:
            st.session_state[f"files.{file_name}"] = StorageUtil.get_file(file_name)

        for image_name in StorageUtil.IMAGE_OPTIONS:
            st.session_state[f"images.{image_name}"] = StorageUtil.get_image(image_name)

    @staticmethod
    def save_states(state_keys: List[str], state_values: List[Any]):
        """Used as callback to save specific state k,v"""
        for state_key, state_value in zip(state_keys, state_values):
            st.session_state[state_key] = state_value

    @staticmethod
    def load_extras():
        """Loads the privacy and license files from disk to state"""
        with open(Config.LICENSE) as license_file:
            st.session_state["files.LICENSE.md"] = license_file.read()

        with open(Config.PRIVACY) as privacy_file:
            st.session_state["files.PRIVACY.md"] = privacy_file.read()

        with open(Config.DOCS) as config_file:
            st.session_state["files.README.md"] = config_file.read()
