"""File contains likes page"""
from utils import StorageMode
from calculations import Likes
import streamlit as st
from pandas import DataFrame
from collections import Counter
from streamlit_extras.row import row
from streamlit_extras.grid import grid
import plotly.express as px


class LikesPage:
    """
    Shows the user their likes page based on uploaded data
    ! This page can only be displayed after a valid archive is uploaded
    """

    likes: Likes

    def most_liked(self, who: str = "server", count: int = 5):
        col_number = 0
        rows = int(count / 5)
        grid_numbers = []

        for row in range(0, rows):
            columns = [1 for i in range(0, 5)]
            grid_numbers.append(columns)

        my_grid = grid(*grid_numbers)

        for entity, like_count in Counter(self.likes.stats[f"likes_per_{who}"]).most_common(count):
            my_grid.metric(entity, like_count)
            col_number += 1

    def __init__(self):
        """When class is called, the page is displayed"""
        self.likes = Likes(StorageMode.state)

        st.title("Your like 👍 stats")
        with st.expander("Totals", expanded=True):
            column_number = 0
            columns = st.columns(self.likes.stats["labelled"].__len__())
            for label, value in self.likes.stats["labelled"].items():
                columns[column_number].metric(label, value)
                column_number += 1

        with st.expander("Server Stats"):
            count = st.number_input("How many servers to show", value=10, min_value=5, step=5, max_value=50, key="server_input")

            st.header(f"Your {count} most liked servers")
            df = DataFrame(
                data=Counter(self.likes.stats["likes_per_server"]).most_common(len(self.likes.stats["likes_per_server"])),
                columns=["Server", "Count"]
            )
            favourite = df.iloc[df["Count"].idxmax()]["Server"]
            least = df.iloc[df["Count"].idxmin()]["Server"]

            fig = px.pie(
                data_frame=df.head(count),
                names="Server",
                values="Count",
                title=f"Seems like {favourite} is your favourite 🌐 💕",
                subtitle=f"...but hope you don't forget about {least} 😪"
            )
            st.plotly_chart(fig)
            self.most_liked("server", count)

        with st.expander("User stats"):
            count = st.number_input("How many users to show", value=10, min_value=5, step=5, max_value=50, key="user_input")

            st.header(f"Your {count} most liked users")
            df = DataFrame(
                data=Counter(self.likes.stats["likes_per_user"]).most_common(len(self.likes.stats["likes_per_user"])),
                columns=["User", "Count"]
            )
            favourite = df.iloc[df["Count"].idxmax()]["User"]
            least = df.iloc[df["Count"].idxmin()]["User"]

            fig = px.pie(
                data_frame=df.head(count),
                names="User",
                values="Count",
                title=f"Seems like {favourite} is your favourite 🧑 💕",
                subtitle=f"...but hope you don't forget about {least} 😪"
            )
            st.plotly_chart(fig)
            self.most_liked("user", count)


LikesPage()
