"""File contains WebUtil used for retrieving data using web requests"""

from logging import Logger, getLogger
from typing import Tuple

import requests

logger: Logger = getLogger("__name__")


class WebUtil:
    """Provides methods for retriving user web data"""

    @staticmethod
    def lookup_account(base_url: str, user_name: str) -> Tuple[int, dict]:
        """Looks up the user at the server"""
        url = f"{base_url}/api/v1/accounts/lookup?acct={user_name}"
        data = requests.get(url=url)
        return data.status_code, data.json()

    @staticmethod
    def get_account(base_url: str, user_id: int) -> Tuple[int, dict]:
        url = f"{base_url}/api/v1/accounts/{user_id}/"
        data = requests.get(url=url)
        return data.status_code, data.json()
