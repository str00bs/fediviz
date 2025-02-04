"""
File contains Likes class, used for:
- Loading
- Transforming
- Displaying

likes data from the users upload.
"""
import pandas as pd
import streamlit as st
from pandas import DataFrame, json_normalize


class Outbox:
    """This class loads, transforms and displays Likes data"""

    contents: dict
    posts: DataFrame
    # TODO: Make not hard-coded
    storage_url: str = "https://media.tech.lgbt"

    def __init__(self, contents: DataFrame, debug: bool = False):
        self.contents = contents
        self.posts = json_normalize(contents["orderedItems"])

        if debug:
            self.debugging()
        self.setup()

    def _filter_posts(self):
        self.posts["published"] = pd.to_datetime(self.posts["published"])
        self.posts = self.posts[self.posts.type != "Announce"]

        attachments = []
        for entry in self.contents["orderedItems"]:
            if entry["type"] == "Create":
                if entry["object"]["attachment"] != []:
                    path = entry["object"]["attachment"][0]["url"].split(".")
                    attachments.append(path[1])

                else:
                    attachments.append("None")
        self.posts["object.attachment"] = attachments

    def _likes_per_month(self):
        likes_per_month = pd.DataFrame(
            self.posts.groupby(pd.Grouper(key="published", freq="MS"))[
                "object.likes.totalItems"
            ].sum()
        )
        likes_per_month.rename(
            columns={"object.likes.totalItems": "likes"}, inplace=True
        )
        likes_per_month.index.name = "month"
        return likes_per_month

    def _likes_per_post(self):
        likes_per_post = pd.DataFrame(
            {
                "published": self.posts["published"].values,
                "likes": self.posts["object.likes.totalItems"].values,
                "post": self.posts["id"].values,
                "attachment": self.posts["object.attachment"].values,
            }
        )
        likes_per_post["post"] = likes_per_post["post"].str.replace(
            "/activity", ""
        )
        return likes_per_post

    def _most_liked_posts(self):
        raise NotImplementedError

    def _most_boosted_posts(self):
        raise NotImplementedError

    def _most_liked_attachment(self, number: int = 10):
        lpp = self._likes_per_post()
        lpp = lpp[lpp.attachment != "None"]
        return lpp["likes"].nlargest(number).reset_index()

    def debugging(self):
        """Displays contents and DF directly on screen"""
        with st.expander("Raw data"):
            st.json(self.contents)
            st.dataframe(self.posts)

    def setup(self):
        """Calls internal data methods and visualizes results"""
        self._filter_posts()
        lpp = self._likes_per_post()
        lpm = self._likes_per_month()

        left_column, right_column = st.columns(2, gap="large")

        with left_column:
            st.header("Likes per post")
            st.bar_chart(
                lpp,
                y="likes",
                x="published",
                y_label="Likes",
                x_label="Published",
            )
            st.text("Dataset")
            st.dataframe(
                lpp,
                column_config={
                    "published": st.column_config.DatetimeColumn(),
                    "likes": st.column_config.NumberColumn(),
                    "post": st.column_config.LinkColumn(display_text="Open"),
                },
            )

        with right_column:
            st.header("Likes Per Month")
            st.line_chart(lpm, y="likes", y_label="Likes", x_label="Month")
            st.text("Dataset")
            st.dataframe(lpm)
