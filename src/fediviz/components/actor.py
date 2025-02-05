"""
File contains actor class, used for:
- Loading
- Transforming
- Displaying

actor data from the users upload.
"""
import html
import streamlit as st
from utils import Uploads, Web
from pandas import DataFrame
from streamlit_extras.stylable_container import stylable_container


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
            df_tags["Description"].append(html.unescape(entry["value"]))

        df = DataFrame(df_tags)
        df.set_index("Tag", inplace=True)
        return df

    def get_links(self):
        """Retrieve and process links for actor"""
        self.http_url = self.contents["url"]

        server, user = self.http_url.split('@')
        server = server.replace('/', '').split('https:')[1]

        self.fedi_url = f"@{user}@{server}"

    def show(self):
        """Calls internal data methods and visualizes results"""
        st.header(self.contents["name"], divider=True)

        with stylable_container("header_container", "{overflow: hidden; max-height: 15vh;}"):
            st.image(Uploads.get_image("header.jpg"))

        left_column, right_column = st.columns(2)

        with left_column:
            st.image(Uploads.get_image("avatar.png"))
        with right_column:
            st.table(self.tags_table())

            nested_left_col, nested_right_col = st.columns(2)

            with nested_left_col:
                st.metric("Followers", 5)
            with nested_right_col:
                st.metric("Follwing", 4)
            st.link_button(
                label=f"Profile: {self.fedi_url}",
                url=self.http_url,
                help="Click open profile on-instance",
                type="primary"
            )

        st.header("Summary", divider=True)
        st.html(self.contents["summary"])
