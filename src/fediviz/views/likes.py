"""File contains likes page"""

from collections import Counter

import plotly.express as px
import streamlit as st
from calculations import Likes
from streamlit_extras.grid import grid
from utils import StorageMode


class LikesPage:
    """
    Shows the user their likes page based on uploaded data
    ! This page can only be displayed after a valid archive is uploaded
    """

    likes: Likes
    css_expander = """
        <style>
            div[data-testid="stExpander"] details {
                background-color: #292938;
                border-radius: 20px;
                border: none;
            }
            div[data-testid="stMetric"] {
                border-radius: 20px;
                padding: 20px;
                border: 1px solid #0D1117;
                background-color: #373E75;
            }
            .main-svg {
                border-radius: 20px;
            }
            p {
                overflow: hidden;
                white-space: nowrap;
                text-overflow: ellipsis;
            }
            p:hover {
                white-space: pre-line;
            }
        <style>
    """

    def most_liked_grid(self, who: str = "server", count: int = 5):
        col_number = 0
        rows = int(count / 5)
        grid_numbers = []

        for _ in range(0, rows):
            columns = [1 for i in range(0, 5)]
            grid_numbers.append(columns)

        my_grid = grid(*grid_numbers)

        for entity, like_count in Counter(
            self.likes.stats[f"likes_per_{who}"]
        ).most_common(count):
            my_grid.metric(entity, like_count)
            col_number += 1

    def __init__(self):
        """When class is called, the page is displayed"""
        self.likes = Likes(StorageMode.state)
        st.markdown(self.css_expander, True)
        st.header("Your Like :material/thumb_up: stats", divider=True)

        with st.expander("Totals", expanded=True):
            column_number = 0
            columns = st.columns(self.likes.stats["labelled"].__len__())
            for label, value in self.likes.stats["labelled"].items():
                columns[column_number].metric(label, value)
                column_number += 1

        with st.expander("Server Stats"):
            count = st.number_input(
                "How many servers to show",
                value=10,
                min_value=5,
                step=5,
                max_value=50,
                key="server_input",
            )

            st.header(f"Your {count} most liked servers", divider=True)
            favourite = self.likes.stats["most_liked_server"]
            least = self.likes.stats["least_liked_server"]

            fig = px.pie(
                data_frame=self.likes.likes_per_server.head(count),
                names="Server",
                values="Count",
                title=f"Seems like {favourite} is your favourite 🌐 💕",
                subtitle=f"...but hope you don't forget about {least} 😪",
            )
            fig.update_layout({"paper_bgcolor": "#373E75"})
            st.plotly_chart(fig, theme=None)
            self.most_liked_grid("server", count)

        with st.expander("User stats"):
            count = st.number_input(
                "How many users to show",
                value=10,
                min_value=5,
                step=5,
                max_value=50,
                key="user_input",
            )

            st.header(f"Your {count} most liked users", divider=True)
            favourite = self.likes.stats["most_liked_user"]
            least = self.likes.stats["least_liked_user"]

            fig = px.pie(
                data_frame=self.likes.likes_per_user.head(count),
                names="User",
                values="Count",
                title=f"Seems like {favourite} is your favourite 🧑 💕",
                subtitle=f"...but hope you don't forget about {least} 😪",
            )
            fig.update_layout({"paper_bgcolor": "#373E75"})
            st.plotly_chart(fig, theme=None)
            self.most_liked_grid("user", count)


LikesPage()
