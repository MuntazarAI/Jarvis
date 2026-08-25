import subprocess
import urllib.parse


def google_search(query: str) -> str:
    """
    Opens a Google search in Firefox.
    """

    query = query.strip()

    # Remove the word "search" only if it is the first word
    if query.lower().startswith("search "):
        query = query[7:].strip()

    url = (
        "https://www.google.com/search?q="
        + urllib.parse.quote_plus(query)
    )

    try:
        subprocess.Popen(
            ["firefox", url],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
            start_new_session=True,
        )

        return f"Searching Google for '{query}'."

    except Exception as e:
        return f"Failed to open browser: {e}"