"""
Module contains app views.
! Cannot be named 'pages' due to automatic streamlit behaviour
"""
from .license import LicensePage
from .privacy import PrivacyPage
from .welcome import WelcomePage
from .profile import ProfilePage

__all__ = [
    "LicensePage",
    "PrivacyPage",
    "WelcomePage",
    "ProfilePage"
]
