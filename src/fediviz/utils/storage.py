"""
File contains StorageUtil used for managing static files and user uploads
"""

import json
from enum import Enum
from typing import Any, Dict, List, Optional
from zipfile import ZipFile

import streamlit as st
from config import Config


class StorageMode(str, Enum):
    """Decides whether to load from archive or state"""

    archive = "archive"
    state = "state"
    default = "default"


class StorageUtil:
    """Provides methods for accessing static files and user uploads"""

    Mode: StorageMode = StorageMode

    FILE_OPTIONS: List[str] = [
        "actor.json",
        "bookmarks.json",
        "likes.json",
        "outbox.json",
    ]
    FILE_EXTRAS: Dict = {
        "LICENSE.md": Config.LICENSE,
        "PRIVACY.md": Config.PRIVACY,
        "README.md": Config.DOCS,
    }
    IMAGE_OPTIONS: List[str] = [
        "header",
        "avatar",
    ]
    IMAGE_DEFAULTS: Dict = {
        "avatar": Config.AVATAR,
        "welcome.step-1": Config.STATIC_DIR.joinpath("undraw-my-files.png"),
        "welcome.step-2": Config.STATIC_DIR.joinpath("undraw-upload.png"),
        "welcome.step-3": Config.STATIC_DIR.joinpath("undraw-folder-files.png"),
    }
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

        for image_name in StorageUtil.IMAGE_DEFAULTS:
            st.session_state[f"defaults.{image_name}"] = None

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

        raise FileNotFoundError(f"name: {name}, mode: {mode}")

    @staticmethod
    def get_image(name: str, mode: StorageMode = StorageMode.archive):
        """Retrieves named image from storage based on mode."""
        match mode:
            case StorageMode.archive:
                archive = ZipFile(st.session_state.uploaded_file)

                full_name: Optional[str] = None

                for item in archive.infolist():
                    if name in item.filename:
                        full_name = item.filename
                if full_name:
                    return archive.read(full_name)

                raise FileNotFoundError(f"name: {name}, mode: {mode}")

            case StorageMode.state:
                if image := st.session_state.get(f"images.{name}", None):
                    return image
                if image := st.session_state.get(f"defaults.{name}", None):
                    return image
                raise FileNotFoundError(f"name: {name}, mode: {mode}")

            case StorageMode.default:
                if image := st.session_state[f"defaults.{name}"]:
                    return image
                raise FileNotFoundError(f"name: {name}, mode: {mode}")
            case _:  # ? No valid modes found
                raise AttributeError(f"{mode} is not a valid StorageMode")

    # ? Callbacks
    @staticmethod
    def save_data():
        for file_name in StorageUtil.FILE_OPTIONS:
            st.session_state[f"files.{file_name}"] = StorageUtil.get_file(file_name)

        for image_name in StorageUtil.IMAGE_OPTIONS:
            try:  # ? To get image from archive
                st.session_state[f"images.{image_name}"] = StorageUtil.get_image(
                    image_name
                )
            except FileNotFoundError:
                try:  # ? To get image from defaults
                    st.session_state[f"images.{image_name}"] = StorageUtil.get_image(
                        image_name, StorageMode.default
                    )
                except KeyError:
                    pass

    @staticmethod
    def save_states(state_keys: List[str], state_values: List[Any]):
        """Used as callback to save specific state k,v"""
        for state_key, state_value in zip(state_keys, state_values):
            st.session_state[state_key] = state_value

    @staticmethod
    def load_extras():
        """Loads the privacy and license files from disk to state"""

        # ? Files
        for name, path in StorageUtil.FILE_EXTRAS.items():
            with open(path) as _file:
                st.session_state[f"files.{name}"] = _file.read()

        # ? Images
        for name, path in StorageUtil.IMAGE_DEFAULTS.items():
            st.session_state[f"defaults.{name}"] = path
