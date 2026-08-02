from tools.browser_tool import BrowserTool

if __name__ == "__main__":
    browser = BrowserTool()

    print(browser.run(
        action="search",
        query="Python decorators",
        limit=3
    ))

    print(browser.run(
        action="open",
        url="https://python.org"
    ))
