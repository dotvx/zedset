#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "click>=8.0.0",
#     "rich>=13.0.0",
# ]
# ///

"""Randomize line order."""

import random
import sys

import click
from rich.console import Console

console = Console()


@click.command()
@click.option('--seed', type=int, help='Random seed for reproducible shuffle')
def main(seed: int | None):
    """Shuffle lines randomly from stdin.

    \b
    Examples:
      cat file.txt | shuffle-lines
      # Random shuffle

      cat file.txt | shuffle-lines --seed 42
      # Reproducible shuffle with seed
    """
    try:
        lines = sys.stdin.read().splitlines()

        if not lines:
            sys.exit(0)

        # Set seed if provided
        if seed is not None:
            random.seed(seed)

        # Shuffle
        random.shuffle(lines)

        # Output
        output = '\n'.join(lines)
        if lines:
            output += '\n'
        sys.stdout.write(output)

    except KeyboardInterrupt:
        console.print("[yellow]Cancelled[/yellow]", file=sys.stderr)
        sys.exit(130)
    except Exception as e:
        console.print(f"[red]Error:[/red] {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
