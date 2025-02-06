"""File contains bookmarks page"""
from utils import StorageMode
from calculations import Bookmarks
import streamlit as st
import plotly.express as px
from collections import Counter
from streamlit_extras.grid import grid


class BookmarksPage:
    """
    Shows the user their bookmarks page based on uploaded data
    ! This page can only be displayed after a valid archive is uploaded
    """

    bookmarks: Bookmarks

    def most_bookmarked_grid(self, who: str = "server", count: int = 5):
        col_number = 0
        rows = int(count / 5)
        grid_numbers = []

        for row in range(0, rows):
            columns = [1 for i in range(0, 5)]
            grid_numbers.append(columns)

        my_grid = grid(*grid_numbers)

        for entity, like_count in Counter(self.bookmarks.stats[f"bookmarks_per_{who}"]).most_common(count):
            my_grid.metric(entity, like_count)
            col_number += 1

    def __init__(self):
        """When class is called, the page is displayed"""
        self.bookmarks = Bookmarks(StorageMode.state)

        st.title("Your Bookmark 📑 stats")
        with st.expander("Totals", expanded=True):
            column_number = 0
            columns = st.columns(self.bookmarks.stats["labelled"].__len__())
            for label, value in self.bookmarks.stats["labelled"].items():
                columns[column_number].metric(label, value)
                column_number += 1

        with st.expander("Server Stats"):
            count = st.number_input("How many servers to show", value=10, min_value=5, step=5, max_value=50, key="server_input")

            st.header(f"Your {count} most bookmarked servers")
            favourite = self.bookmarks.stats["most_bookmarked_server"]
            least = self.bookmarks.stats["least_bookmarked_server"]

            fig = px.pie(
                data_frame=self.bookmarks.bookmarks_per_server.head(count),
                names="Server",
                values="Count",
                title=f"Seems like {favourite} is where it's interesting 🔍",
                subtitle=f"but posts on {least} are still worth checking out 🏃"
            )
            st.plotly_chart(fig)
            self.most_bookmarked_grid("server", count)

        with st.expander("User stats"):
            count = st.number_input("How many users to show", value=10, min_value=5, step=5, max_value=50, key="user_input")

            st.header(f"Your {count} most bookmarked users")
            favourite = self.bookmarks.stats["most_bookmarked_user"]
            least = self.bookmarks.stats["least_bookmarked_user"]

            fig = px.pie(
                data_frame=self.bookmarks.bookmarks_per_user.head(count),
                names="User",
                values="Count",
                title=f"For you, posts by {favourite} is worth saving 💾",
                subtitle=f"...but still you still read posts from {least} 👓"
            )
            st.plotly_chart(fig)
            self.most_bookmarked_grid("user", count)



BookmarksPage()
