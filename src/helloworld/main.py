#!/usr/bin/env python3

def hello(name: str = "World") -> str:
    """Return a friendly greeting."""
    return f"Hello, {name}!"


def main() -> None:
    """Entry point for `python -m helloworld.main`."""
    print(hello())


if __name__ == "__main__":
    main()

