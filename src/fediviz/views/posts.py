"""File contains posts page"""

import plotly.express as px
import streamlit as st
from calculations import Outbox
from styles import Styles
from utils import StorageMode


class PostsPage:
    """
    Shows the user their posts page based on uploaded data
    ! This page can only be displayed after a valid archive is uploaded
    """

    posts: Outbox

    def __init__(self):
        """When class is called, the page is displayed"""
        self.posts = Outbox(StorageMode.state)
        st.header("Your Post :material/mail: stats", divider=True)
        st.markdown(Styles.posts, True)

        with st.expander("Likes per post"):
            self.posts.likes_per_post.columns = (
                self.posts.likes_per_post.columns.str.capitalize()
            )
            st.header("Likes per post", divider=True)
            fig = px.line(self.posts.likes_per_post, x="Published", y="Likes")
            fig.update_traces(line_color="#636EFA")
            fig.update_layout(
                {
                    "paper_bgcolor": "#373E75",
                    "plot_bgcolor": "#373E75",
                    "yaxis_gridcolor": "#292938",
                }
            )
            st.plotly_chart(fig, theme=None)
            st.header("Dataset", divider=True)
            st.dataframe(
                self.posts.likes_per_post,
                column_config={
                    "Published": st.column_config.DatetimeColumn(),
                    "Likes": st.column_config.NumberColumn(),
                    "Post": st.column_config.LinkColumn(display_text="Open"),
                },
                use_container_width=True,
            )

        with st.expander("Likes per Month"):
            self.posts.likes_per_month.reset_index(inplace=True)
            self.posts.likes_per_month.columns = (
                self.posts.likes_per_month.columns.str.capitalize()
            )
            st.header("Likes per Month", divider=True)
            fig = px.line(
                self.posts.likes_per_month,
                x="Month",
                y="Likes",
            )
            fig.update_traces(line_color="#636EFA")
            fig.update_layout(
                {
                    "paper_bgcolor": "#373E75",
                    "plot_bgcolor": "#373E75",
                    "yaxis_gridcolor": "#292938",
                    "xaxis_tickformat": "%b %y",
                    "yaxis_tickcolor": "pink",
                }
            )
            st.plotly_chart(fig, theme=None)
            st.header("Dataset", divider=True)
            st.dataframe(
                self.posts.likes_per_month,
                column_config={
                    "Month": st.column_config.DateColumn(),
                    "Likes": st.column_config.NumberColumn(),
                },
                use_container_width=True,
            )


PostsPage()
