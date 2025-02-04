"""
File contains actor class, used for:
- Loading
- Transforming
- Displaying

actor data from the users upload.
"""
import streamlit as st
from utils import Uploads
from pandas import DataFrame
from datetime import datetime


class Actor:
    """This class loads, transforms and displays Actor data"""

    contents: dict
    http_url: str
    fedi_url: str
    name: str

    def __init__(self):
        self.contents = Uploads.get_file("actor.json")
        self.get_links()

        self.show()

    def tags_table(self) -> DataFrame:
        """Retrieve, process and return actor tags"""
        df_tags = {"Tag": [], "Description": []}
        for entry in self.contents["attachment"]:
            df_tags["Tag"].append(entry["name"])
            df_tags["Description"].append(entry["value"])

        df = DataFrame(df_tags)
        df.set_index("Tag", inplace=True)
        return df

    def get_links(self):
        """Retrieve and process links for actor"""
        self.http_url = self.contents["url"]

        server, user = self.http_url.split('@')
        server = server.replace('/', '').split('https:')[1]

        self.fedi_url = f"@{server}@{user}"

    def show(self):
        """Calls internal data methods and visualizes results"""
        with st.container():
            st.header(self.contents["name"], divider=True)
            left_column, right_column = st.columns(2)
            with left_column:
                st.image(Uploads.get_image("avatar.png"))
                st.link_button(
                    label=f"Profile: {self.fedi_url}",
                    url=self.http_url,
                    help="Click open profile on-instance",
                    type="primary"
                )
            with right_column:
                st.image(Uploads.get_image("header.jpg"))
                st.table(self.tags_table())

            with st.container(border=True):
                st.header("Summary", divider=True)
                st.html(self.contents["summary"])
