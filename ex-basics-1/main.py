from typing import Optional
import typer
from rich import print

app = typer.Typer(help="Simple CLI for greeting people.")

@app.command()
def hello(name: Optional[str] = typer.Argument(None, help="Name to greet")) -> None:
    """
    CLI command that prints a greeting.
    """
    target: str = name or "world"
    print(f":wave: [bold green]Hello {target}![/bold green]")

if __name__ == "__main__":
    app()
