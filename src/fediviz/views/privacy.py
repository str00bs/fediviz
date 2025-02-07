"""File contains privacy page"""

from components import show_privacy


class PrivacyPage:
    """Shows the user the app's privacy statement"""

    def __init__(self):
        """When class is called, the page is displayed"""
        show_privacy()


PrivacyPage()
