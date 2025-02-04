"""Application main file"""
from views import Layout, Outbox, Uploads
from dotenv import load_dotenv

contents: dict


if __name__ == "__main__":
    load_dotenv()
    contents = Uploads.get()  # TODO: Update once uploaded data is used

    # ? Setup pages
    Layout()
    Outbox(contents=contents, debug=True)
