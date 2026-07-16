import webbrowser

from duckduckgo_search import DDGS

from tools.base import Tool


class BrowserTool(Tool):

    name = "browser"

    description = (
        "Search the web and open websites."
    )

    def run(self, action, **kwargs):

        try:

            if action == "search":

                query = kwargs["query"]

                limit = kwargs.get("limit", 5)

                results = []

                with DDGS() as ddgs:

                    for item in ddgs.text(
                        query,
                        max_results=limit
                    ):

                        results.append({
                            "title": item.get("title"),
                            "url": item.get("href"),
                            "body": item.get("body")
                        })

                return results

            elif action == "open":

                url = kwargs["url"]

                if not url.startswith("http"):
                    url = "https://" + url

                webbrowser.open(url)

                return {
                    "success": True,
                    "url": url
                }

            else:

                return {
                    "success": False,
                    "error": f"Unknown action '{action}'"
                }

        except Exception as e:

            return {
                "success": False,
                "error": str(e)
            }


browser = BrowserTool()