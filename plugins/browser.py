from core.browser import google_search


def search(query):

    return google_search(query)


def register(manager):

    manager.register("browser", search)