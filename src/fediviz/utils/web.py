"""File contains class used for retrieving user data from the web"""
import json
from typing import Tuple
from logging import getLogger, Logger
from zipfile import ZipFile
import streamlit as st
import requests


logger: Logger = getLogger("__name__")


class Web:
    """This class manages user web data from mastodon servers"""

    @staticmethod
    def lookup_account(base_url: str, user_name: str) -> Tuple[int, dict]:
        """Looks up the user at the server"""
        url = f"{base_url}/api/v1/accounts/lookup?acct={user_name}"
        data = requests.get(url=url)
        return data.status_code, data.json()

    @staticmethod
    def get_account(base_url: str, user_id: int):
        url = f"{base_url}/api/v1/accounts/{user_id}"
        data = requests.get(url=url)
        return data.status_code, data.json()
