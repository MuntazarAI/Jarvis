from core.system import open_application


def run(target):

    return open_application(target)


def register(manager):

    manager.register("system", run)