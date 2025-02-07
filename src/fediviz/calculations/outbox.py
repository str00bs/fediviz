"""File contains outbox class, used for extracting & loading data from outbox.json"""

import pandas as pd
from pandas import DataFrame, json_normalize
from utils import StorageMode, StorageUtil


class Outbox:
    """This class is used to extract & transform outbox data"""

    # ? Static properties
    FILE_NAME: str = "outbox.json"
    data_file: dict
    mode: StorageMode

    # ? Results
    likes_per_post: DataFrame
    likes_per_month: DataFrame

    def __init__(self, mode: StorageMode = StorageMode.state):
        self.data_file = StorageUtil.get_file(self.FILE_NAME, mode)
        self.posts = json_normalize(self.data_file["orderedItems"])
        self.mode = mode

        self.filter_posts()
        self.extract_likes_per_post()
        self.extract_likes_per_month()

    def filter_posts(self):
        self.posts["published"] = pd.to_datetime(self.posts["published"])
        self.posts = self.posts[self.posts.type != "Announce"]

        attachments = []
        for entry in self.data_file["orderedItems"]:
            if entry["type"] == "Create":
                if entry["object"]["attachment"] != []:
                    path = entry["object"]["attachment"][0]["url"].split(".")
                    attachments.append(path[1])

                else:
                    attachments.append("None")
        self.posts["object.attachment"] = attachments

    def extract_posts_by_day(self):
        raise NotImplementedError

    def extract_posts_by_hour(self):
        raise NotImplementedError

    def extract_likes_per_month(self):
        likes_per_month = pd.DataFrame(
            self.posts.groupby(pd.Grouper(key="published", freq="MS"))[
                "object.likes.totalItems"
            ].sum()
        )
        likes_per_month.rename(
            columns={"object.likes.totalItems": "likes"}, inplace=True
        )
        likes_per_month.index.name = "month"
        self.likes_per_month = likes_per_month

    def extract_likes_per_post(self):
        likes_per_post = pd.DataFrame(
            {
                "published": self.posts["published"].values,
                "likes": self.posts["object.likes.totalItems"].values,
                "post": self.posts["id"].values,
                "attachment": self.posts["object.attachment"].values,
            }
        )
        likes_per_post["post"] = likes_per_post["post"].str.replace("/activity", "")
        self.likes_per_post = likes_per_post

    def extract_most_liked_posts(self):
        raise NotImplementedError

    def extract_most_boosted_posts(self):
        raise NotImplementedError

    def extract_most_liked_attachment(self, number: int = 10):
        lpp = self._likes_per_post()
        lpp = lpp[lpp.attachment != "None"]
        return lpp["likes"].nlargest(number).reset_index()
