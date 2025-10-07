#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "click>=8.0.0",
#     "rich>=13.0.0",
# ]
# ///

"""Reverse the order of lines in text."""

import sys

import click
from rich.console import Console

console = Console()


@click.command()
def main():
    """Reverse line order from stdin.

    \b
    Example:
      echo -e "1\\n2\\n3" | inv-order-lines
      # Output: 3, 2, 1
    """
    try:
        lines = sys.stdin.read().splitlines()
        lines.reverse()

        # Output to stdout (preserves trailing newline if input had one)
        output = "\n".join(lines)
        if lines:  # Only add final newline if there was input
            output += "\n"
        sys.stdout.write(output)

    except KeyboardInterrupt:
        console.print("[yellow]Cancelled[/yellow]", file=sys.stderr)
        sys.exit(130)
    except Exception as e:
        console.print(f"[red]Error:[/red] {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
