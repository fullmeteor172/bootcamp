from typing import Optional


def hello(name: Optional[str] = None) -> None:
    """
    Print a hello message with the provided name or 'world' by default.

    Args:
        name (Optional[str]): Name to greet. Defaults to None (prints 'world').
    """
    target: str = name or "world"
    print(f"Hello {target}")
