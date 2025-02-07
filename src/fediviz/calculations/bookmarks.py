"""
File contains bookmarks class,
used for extracting & loading data from bookmarks.json
"""

from collections import Counter

from pandas import DataFrame
from utils import StorageMode, StorageUtil


class Bookmarks:
    """This class is used to extract & transform bookmarks data"""

    # ? Static properties
    FILE_NAME: str = "bookmarks.json"
    data_file: dict
    mode: StorageMode

    # ? Dynamic (data) properties
    count: int
    data: dict
    bookmarks_by_server: dict
    bookmarks_by_account: dict

    stats: dict
    bookmarks_per_server: DataFrame
    bookmarks_per_user: DataFrame

    def __init__(self, mode: StorageMode = StorageMode.state):
        self.data_file = StorageUtil.get_file(self.FILE_NAME, mode)
        self.mode = mode
        # self.data = {}
        # self.extract_count()
        # self.extract_counts_by()

        self.stats = {}
        self.extract_bookmarks_per()
        self.extract_most_least()

    def extract_count(self):
        self.count = len(self.data_file["orderedItems"])

    # def extract_counts_by(self):
    #     data = {
    #         "bookmarks_by_server": {},
    #         "bookmarks_by_account": {}
    #     }
    #     for entry in self.data_file["orderedItems"]:
    #         entry = entry.split("https://")[1]
    #         entry = entry.split("/")
    #         # ? [server, 'users' || random, user, 'statuses', status_id]

    #         if entry[0] in data["bookmarks_by_server"].keys():
    #             data["bookmarks_by_server"][entry[0]] += 1
    #         else:
    #             data["bookmarks_by_server"][entry[0]] = 1

    #         if entry[1] == "users":
    #             if entry[2] in data["bookmarks_by_account"].keys():
    #                 data["bookmarks_by_account"][entry[2]] += 1
    #             else:
    #                 data["bookmarks_by_account"][entry[2]] = 1
    #         else:
    #             if "user_not_in_url" not in data["bookmarks_by_account"].keys():
    #                 data["bookmarks_by_account"]['user_not_in_url'] = 1
    #             else:
    #                 data["bookmarks_by_account"]['user_not_in_url'] += 1

    #     for key, value in data.items():
    #         self.data.update({key: value})

    #     self.bookmarks_by_server = data["bookmarks_by_server"]
    #     self.bookmarks_by_account = data["bookmarks_by_account"]

    def extract_bookmarks_per(self):
        bookmarks_per_server = {}
        bookmarks_per_user = {}
        for like in self.data_file["orderedItems"]:
            server = like.split("https://")[1].split("/")[0]
            try:
                user = like.split("users/")[1].split("/")[0]
            except IndexError:
                continue

            bookmarks_per_server[server] = 0
            bookmarks_per_user[f"@{user}@{server}"] = 0

        for like in self.data_file["orderedItems"]:
            server = like.split("https://")[1].split("/")[0]
            try:
                user = like.split("users/")[1].split("/")[0]
            except IndexError:
                continue

            bookmarks_per_server.update({server: bookmarks_per_server[server] + 1})
            bookmarks_per_user.update(
                {f"@{user}@{server}": bookmarks_per_user[f"@{user}@{server}"] + 1}
            )

        self.stats.update(
            {
                "bookmarks_per_server": bookmarks_per_server,
                "bookmarks_per_user": bookmarks_per_user,
                "labelled": {
                    "Unique servers bookmarked": len(bookmarks_per_server.keys()),
                    "Total bookmarks": sum(bookmarks_per_server.values()),
                },
            }
        )

        # ? Create graph compatible DFs
        self.bookmarks_per_server = DataFrame(
            data=Counter(self.stats["bookmarks_per_server"]).most_common(
                len(self.stats["bookmarks_per_server"])
            ),
            columns=["Server", "Count"],
        )
        self.bookmarks_per_user = DataFrame(
            data=Counter(self.stats["bookmarks_per_user"]).most_common(
                len(self.stats["bookmarks_per_user"])
            ),
            columns=["User", "Count"],
        )

    def extract_most_least(self):
        self.stats["most_bookmarked_server"] = self.bookmarks_per_server.iloc[
            self.bookmarks_per_server["Count"].idxmax()
        ]["Server"]
        self.stats["least_bookmarked_server"] = self.bookmarks_per_server.iloc[
            self.bookmarks_per_server["Count"].idxmin()
        ]["Server"]
        self.stats["most_bookmarked_user"] = self.bookmarks_per_user.iloc[
            self.bookmarks_per_user["Count"].idxmax()
        ]["User"]
        self.stats["least_bookmarked_user"] = self.bookmarks_per_user.iloc[
            self.bookmarks_per_user["Count"].idxmin()
        ]["User"]
