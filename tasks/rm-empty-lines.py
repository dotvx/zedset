#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "click>=8.0.0",
#     "rich>=13.0.0",
# ]
# ///

"""Collapse consecutive empty lines to a maximum count."""

import sys

import click
from rich.console import Console

console = Console()


@click.command()
@click.argument("max_empty", type=int, default=0)
def main(max_empty: int):
    """Collapse consecutive empty lines to maximum MAX_EMPTY.

    MAX_EMPTY: Maximum consecutive empty lines allowed (default: 0)

    \b
    Examples:
      # Remove all empty lines
      cat file.txt | rm-empty-lines 0

      # Allow max 1 empty line (preserve paragraphs)
      cat file.txt | rm-empty-lines 1

      # Allow max 2 consecutive empty lines
      cat file.txt | rm-empty-lines 2
    """
    try:
        if max_empty < 0:
            console.print("[red]Error:[/red] max_empty must be >= 0", file=sys.stderr)
            sys.exit(2)

        lines = sys.stdin.read().splitlines()
        result = []
        empty_count = 0

        for line in lines:
            if line.strip() == "":  # Empty or whitespace-only line
                empty_count += 1
                if empty_count <= max_empty:
                    result.append(line)
            else:
                empty_count = 0
                result.append(line)

        # Output to stdout (preserves trailing newline if input had one)
        output = "\n".join(result)
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
