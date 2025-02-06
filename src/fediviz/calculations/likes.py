"""File contains likes class, used for extracting & loading data from likes.json"""
from typing import Tuple, List
import streamlit as st
from utils import StorageUtil, StorageMode
from pandas import DataFrame
from collections import Counter
from streamlit_extras.row import row
from streamlit_extras.grid import grid
import plotly.express as px


class Likes:
    """This class is used to extract & transform bookmarks data"""

    # ? Static properties
    FILE_NAME: str = "bookmarks.json"
    data_file: dict
    mode: StorageMode

    def __init__(self, mode: StorageMode = StorageMode.state):
        self.data_file = StorageUtil.get_file(self.FILE_NAME, mode)
        self.mode = mode

    def extract_stats(self, count: int = 5):
        """Method extracts """

        likes_per_server = {}
        likes_per_user = {}
        for like in self.likes:
            server = like.split("https://")[1].split("/")[0]
            try:
                user = like.split("users/")[1].split("/")[0]
            except IndexError:
                continue

            likes_per_server[server] = 0
            likes_per_user[f"@{user}@{server}"] = 0

        for like in self.likes:
            server = like.split("https://")[1].split("/")[0]
            try:
                user = like.split("users/")[1].split("/")[0]
            except IndexError:
                continue

            likes_per_server.update({server: likes_per_server[server] + 1})
            likes_per_user.update({f"@{user}@{server}": likes_per_user[f"@{user}@{server}"] + 1})

        self.stats.update({
            "likes_per_server": likes_per_server,
            "likes_per_user": likes_per_user,
            "most_liked_server": "",
            "least_liked_server": "",
            "most_liked_user": "",
            "least_liked_user": "",
            "labelled": {
                "Unique servers liked": len(likes_per_server.keys()),
                "Total likes": sum(likes_per_server.values())
            }
        })

    def most_liked(self, who: str = "server", count: int = 5):
        col_number = 0
        rows = int(count / 5)
        grid_numbers = []

        for row in range(0, rows):
            columns = [1 for i in range(0, 5)]
            grid_numbers.append(columns)

        my_grid = grid(*grid_numbers)

        for entity, like_count in Counter(self.stats[f"likes_per_{who}"]).most_common(count):
            my_grid.metric(entity, like_count)
            col_number += 1

    def show(self):
        st.title("Your like 👍 stats")
        with st.expander("Totals", expanded=True):
            column_number = 0
            columns = st.columns(self.stats["labelled"].__len__())
            for label, value in self.stats["labelled"].items():
                columns[column_number].metric(label, value)
                column_number += 1

        with st.expander("Server Stats"):
            count = st.number_input("How many servers to show", value=10, min_value=5, step=5, max_value=50, key="server_input")

            st.header(f"Your {count} most liked servers")
            df = DataFrame(
                data=Counter(self.stats["likes_per_server"]).most_common(len(self.stats["likes_per_server"])),
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
                data=Counter(self.stats["likes_per_user"]).most_common(len(self.stats["likes_per_user"])),
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
