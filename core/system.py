import subprocess


APPS = {
    "firefox": "firefox",
    "calculator": "gnome-calculator",
    "files": "nautilus",

    "terminal": "gnome-terminal",

    "vs code": "code",
    "vscode": "code",
    "code": "code",
}


def open_application(name: str):

    name = name.lower().strip()

    command = APPS.get(name)

    if command is None:
        return f"I don't know how to open '{name}'."

    try:
        subprocess.Popen(
            [command],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
        )

        return f"Opening {name.title()}."

    except Exception as e:
        return f"Failed to open {name}: {e}"
