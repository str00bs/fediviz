"""File contains app styles"""


class Styles:
    """Contains app styles in css format"""

    bookmarks: str = """
        <style>
            div[data-testid="stExpander"] details {
                background-color: #292938;
                border-radius: 20px;
                border: none;
            }
            div[data-testid="stMetric"] {
                border-radius: 20px;
                padding: 20px;
                border: 1px solid #0D1117;
                background-color: #373E75;
            }
            .main-svg {
                border-radius: 20px;
            }
            p {
                overflow: hidden;
                white-space: nowrap;
                text-overflow: ellipsis;
            }
            p:hover {
                white-space: pre-line;
            }
        <style>
    """
    likes: str = """
        <style>
            div[data-testid="stExpander"] details {
                background-color: #292938;
                border-radius: 20px;
                border: none;
            }
            div[data-testid="stMetric"] {
                border-radius: 20px;
                padding: 20px;
                border: 1px solid #0D1117;
                background-color: #373E75;
            }
            .main-svg {
                border-radius: 20px;
            }
            p {
                overflow: hidden;
                white-space: nowrap;
                text-overflow: ellipsis;
            }
            p:hover {
                white-space: pre-line;
            }
        <style>
    """
    posts: str = """
        <style>
            div[data-testid="stExpander"] details {
                background-color: #292938;
                border-radius: 20px;
                border: none;
            }
            div[data-testid="stMetric"] {
                border-radius: 20px;
                padding: 20px;
                border: 1px solid #0D1117;
                background-color: #373E75;
            }
            .main-svg {
                border-radius: 20px;
            }
            p {
                overflow: hidden;
                white-space: nowrap;
                text-overflow: ellipsis;
            }
            p:hover {
                white-space: pre-line;
            }
        <style>
    """
    profile: str = """
        [data-testid="stImageContainer"] img {
            border-radius: 10%;
            width: 20vw;
            margin-top: 50px;
        }
    """
    welcome: dict = {
        "container": """
            [data-testid="stText"] div{
                display: flex;
                justify-content: flex-end;
                width: 100%;
            }
        """,
        "expander": """
            <style>
                div[data-testid="stExpander"] details {
                    background-color: #292938;
                    border-radius: 20px;
                    border: none;
                },
            <style>
        """,
    }
