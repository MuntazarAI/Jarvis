from rich.console import Console

console = Console()


def info(message):
    console.print(f"[cyan][INFO][/cyan] {message}")


def success(message):
    console.print(f"[green][SUCCESS][/green] {message}")


def error(message):
    console.print(f"[red][ERROR][/red] {message}")
