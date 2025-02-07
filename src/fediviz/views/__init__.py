"""
Module contains app views.
! Cannot be named 'pages' due to automatic streamlit behaviour
"""

from .license import LicensePage
from .privacy import PrivacyPage
from .profile import ProfilePage
from .welcome import WelcomePage

__all__ = ["LicensePage", "PrivacyPage", "WelcomePage", "ProfilePage"]
