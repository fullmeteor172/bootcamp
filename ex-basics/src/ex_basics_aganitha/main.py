from typing import Optional
import typer
from rich import print

app = typer.Typer()

@app.command()
def hello(name: str = typer.Argument("world", help="Name to greet")) -> None:
    """
    CLI command that prints a greeting.
    """
    print(f":wave: [bold green]Hello {name}![/bold green]")

if __name__ == "__main__":
    app()
