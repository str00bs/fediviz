"""File contains welcome page"""

import streamlit as st
from calculations import Actor
from config import Config
from streamlit_extras.stylable_container import stylable_container
from styles import Styles
from utils import StorageUtil, WebUtil


class WelcomePage:
    """Welcomes the user and provides instructions for usage"""

    actor: Actor

    def __init__(self):
        """When class is called, the page is displayed"""
        st.markdown(
            Styles.welcome["expander"], True
        )  # ? This removes borders for the whole page

        with stylable_container("WelcomePage.body", Styles.welcome["container"]):
            with st.expander("Step 1/3: Request your export", expanded=True):
                st.subheader("Request your export", divider=True)
                st.image(StorageUtil.get_image("welcome.step-1", "state"))
                st.markdown(
                    """
                    1. Go to your mastodon instance
                    2. Click -> Menu -> Preferences
                    3. Click -> Import and export
                    4. Click -> Download your archive
                    <!-- Override styling, it will apply on this page -->
                    <style>
                    [data-testid="stMarkdownContainer"] ol{
                        list-style-position: inside;
                    }
                    </style>
                    """,
                    unsafe_allow_html=True,
                )

                first_left_column, first_right_column = st.columns(2)

                with first_left_column.popover(
                    label="Where to find your preferences",
                    icon=":material/help:",
                ):
                    st.image(
                        image=f"{Config.STATIC_DIR}/example_menu_preferences.png",
                        caption="Visual example of menu and preferences location",
                    )
                with first_right_column.popover(
                    label="Where to find export in settings",
                    icon=":material/help:",
                ):
                    st.image(
                        image=f"{Config.STATIC_DIR}/example_export_page.png",
                        caption="Visual example of export location in preferences",
                    )

            with st.expander("Step 2/3: Upload your archive"):
                st.subheader("Upload your archive", divider=True)
                st.image(StorageUtil.get_image("welcome.step-2", "state"))
                result = st.file_uploader(
                    label="Upload your `export.zip`", key="uploaded_file"
                )
                if result is not None:
                    st.success("Successfully uploaded export", icon="✅")
                    btn_context = st.button(
                        "Continue now",
                        on_click=StorageUtil.save_data,
                        type="primary",
                    )
                    if btn_context:
                        st.session_state["toggles.has_completed_steps"] = True
                        st.rerun()
                    self.actor = Actor(mode="archive")
                    st.session_state["welcome.user_url"] = self.actor.http_url

            with st.expander("Optional[Step 3/3]: Request your followers/follows"):
                st.subheader("Request your followers/follows", divider=True)
                st.image(StorageUtil.get_image("welcome.step-3", "state"))
                st.markdown(
                    """
                    These are not included in the export by default, so if we want to show these metrics,
                    we have to try to ask your server if they can share that data with us.

                    This is done with a lookup request to your server asking for your followers/follows
                    """  # noqa
                )
                if st.session_state["welcome.user_url"] is not None:
                    if st.button(
                        "Send requests",
                        key="Welcome.Button.SendRequest",
                        type="primary",
                    ):
                        base_url, user_name = st.session_state[
                            "welcome.user_url"
                        ].split("/@")
                        lookup_result_code, lookup_results = WebUtil.lookup_account(
                            base_url, user_name
                        )
                        if lookup_result_code == 200:
                            StorageUtil.save_states(
                                state_keys=StorageUtil.USER_OPTIONS,
                                state_values=[
                                    lookup_results[v.strip("user.")]
                                    for v in StorageUtil.USER_OPTIONS
                                ],
                            )
                            st.session_state["toggles.has_followers"] = True
                            st.session_state["toggles.has_completed_steps"] = True
                            st.success(
                                "Successfully retrieved your followers/follows",
                                icon="✅",
                            )
                            st.text("What did we just retrieve?")
                            st.json(lookup_results, expanded=False)
                            if st.button(
                                "Continue",
                                key="Welcome.Button.Continue",
                                on_click=StorageUtil.save_data,
                                type="primary",
                            ):
                                st.session_state["toggles.has_completed_steps"] = True
                                st.rerun()
                        else:
                            st.error(
                                "Could not lookup that combination of Server URL and username",  # noqa
                                icon="❌",
                            )
                else:
                    st.warning("You must upload a valid archive first", icon="⚠️")


WelcomePage()
