"""File contains posts page"""
from utils import StorageMode
from calculations import Outbox
import streamlit as st


class PostsPage:
    """
    Shows the user their posts page based on uploaded data
    ! This page can only be displayed after a valid archive is uploaded
    """

    posts: Outbox

    def __init__(self):
        """When class is called, the page is displayed"""
        self.posts = Outbox(StorageMode.state)
        st.header("Your Posts")

        left_column, right_column = st.columns(2, gap="large")

        with left_column:
            st.header("Likes per post")
            st.bar_chart(
                self.posts.likes_per_post,
                y="likes",
                x="published",
                y_label="Likes",
                x_label="Published",
            )
            st.text("Dataset")
            st.dataframe(
                self.posts.likes_per_post,
                column_config={
                    "published": st.column_config.DatetimeColumn(),
                    "likes": st.column_config.NumberColumn(),
                    "post": st.column_config.LinkColumn(display_text="Open"),
                },
            )

        with right_column:
            st.header("Likes Per Month")
            st.line_chart(self.posts.likes_per_month, y="likes", y_label="Likes", x_label="Month")
            st.text("Dataset")
            st.dataframe(self.posts.likes_per_month)


PostsPage()
