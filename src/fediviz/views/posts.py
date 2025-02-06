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
        st.header("Your Post :material/mail: stats")

        with st.expander("Likes per post"):
            self.posts.likes_per_post.columns = self.posts.likes_per_post.columns.str.capitalize()
            st.header("Likes per post")
            st.bar_chart(
                self.posts.likes_per_post,
                y="Likes",
                x="Published",
                y_label="Likes",
                x_label="Published",
            )
            st.text("Dataset")
            st.dataframe(
                self.posts.likes_per_post,
                column_config={
                    "Published": st.column_config.DatetimeColumn(),
                    "Likes": st.column_config.NumberColumn(),
                    "Post": st.column_config.LinkColumn(display_text="Open"),
                },
                use_container_width=True
            )

        with st.expander("Likes per Month"):
            self.posts.likes_per_month.reset_index(inplace=True)
            self.posts.likes_per_month.columns = self.posts.likes_per_month.columns.str.capitalize()
            st.header("Likes per Month")
            st.line_chart(self.posts.likes_per_month, y="Likes", y_label="Likes", x_label="Month")
            st.text("Dataset")
            st.dataframe(
                self.posts.likes_per_month,
                column_config={
                    "Month": st.column_config.DateColumn(),
                    "Likes": st.column_config.NumberColumn()
                },
                use_container_width=True
            )


PostsPage()
