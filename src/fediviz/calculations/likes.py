"""File contains likes class, used for extracting & loading data from likes.json"""
from typing import Tuple, List
import streamlit as st
from utils import StorageUtil, StorageMode
from pandas import DataFrame
from collections import Counter


class Likes:
    """This class is used to extract & transform likes data"""

    # ? Static properties
    FILE_NAME: str = "likes.json"
    data_file: dict
    mode: StorageMode
    stats: dict

    likes_per_server: DataFrame
    likes_per_user: DataFrame

    def __init__(self, mode: StorageMode = StorageMode.state):
        self.data_file = StorageUtil.get_file(self.FILE_NAME, mode)
        self.mode = mode
        self.stats = {}
        self.extract_likes_per()
        self.extract_most_least()

    def extract_likes_per(self):
        likes_per_server = {}
        likes_per_user = {}
        for like in self.data_file["orderedItems"]:
            server = like.split("https://")[1].split("/")[0]
            try:
                user = like.split("users/")[1].split("/")[0]
            except IndexError:
                continue

            likes_per_server[server] = 0
            likes_per_user[f"@{user}@{server}"] = 0

        for like in self.data_file["orderedItems"]:
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
            "labelled": {
                "Unique servers liked": len(likes_per_server.keys()),
                "Total likes": sum(likes_per_server.values())
            }
        })

        # ? Create graph compatible DFs
        self.likes_per_server = DataFrame(
            data=Counter(self.stats["likes_per_server"]).most_common(len(self.stats["likes_per_server"])),
            columns=["Server", "Count"]
        )
        self.likes_per_user = DataFrame(
            data=Counter(self.stats["likes_per_user"]).most_common(len(self.stats["likes_per_user"])),
            columns=["User", "Count"]
        )

    def extract_most_least(self):
        self.stats["most_liked_server"] = self.likes_per_server.iloc[self.likes_per_server["Count"].idxmax()]["Server"]
        self.stats["least_liked_server"] = self.likes_per_server.iloc[self.likes_per_server["Count"].idxmin()]["Server"]
        self.stats["most_liked_user"] = self.likes_per_user.iloc[self.likes_per_user["Count"].idxmax()]["User"]
        self.stats["least_liked_user"] = self.likes_per_user.iloc[self.likes_per_user["Count"].idxmin()]["User"]
