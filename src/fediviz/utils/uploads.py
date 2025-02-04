"""File contains class used for uploading user data"""
import json
from logging import getLogger, Logger
from zipfile import ZipFile
import streamlit as st


logger: Logger = getLogger("__name__")


class Uploads:
    """This class manages user data uploads"""

    @staticmethod
    def get_file(name: str) -> dict:
        """Gets JSON datafile from user archive and returns it as a dict"""
        file = ZipFile(st.session_state.uploaded_file).read(name)
        return json.loads(file.decode())

    @staticmethod
    def get_image(name: str):
        """Gets image from user archive"""
        archive = ZipFile(st.session_state.uploaded_file).read(name)
        return archive

    @staticmethod
    def has_file() -> bool:
        """Checks if a valid archive file has been uploaded"""
        return all([
            st.session_state.get("uploaded_file") is not None
        ])

    @staticmethod
    def show():
        """Displays file uploader"""
        st.header("Upload archive")
        st.file_uploader(
            label="Upload your `export.zip`",
            key="uploaded_file"
        )
