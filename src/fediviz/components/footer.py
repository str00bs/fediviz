"""File contains reuseable footer component"""
from streamlit_extras.bottom_container import bottom
from streamlit_extras.mention import mention


def show_footer():
    """Reuseable footer component"""
    with bottom():
        mention(
            label="github.com/str00bs/fediviz",
            icon="github",
            url="https://github.com/str00bs/fediviz",
        )
