#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "click>=8.0.0",
#     "rich>=13.0.0",
# ]
# ///

"""Add or remove line numbers."""

import re
import sys

import click
from rich.console import Console

console = Console()


@click.command()
@click.option('--add', 'mode', flag_value='add', default=True, help='Add line numbers (default)')
@click.option('--remove', 'mode', flag_value='remove', help='Remove line numbers')
@click.option('--format', 'num_format', default='%d. ', help='Number format for --add (default: "%d. ")')
@click.option('--start', type=int, default=1, help='Starting line number (default: 1)')
@click.option('--step', type=int, default=1, help='Increment step (default: 1)')
def main(mode: str, num_format: str, start: int, step: int):
    """Add or remove line numbers from text.

    \b
    Examples:
      cat file.txt | line-numbers
      # Add line numbers: 1. , 2. , ...

      cat file.txt | line-numbers --format "%03d: "
      # Format: 001: , 002: , ...

      cat numbered.txt | line-numbers --remove
      # Strip line numbers

      cat file.txt | line-numbers --start 100 --step 10
      # Number: 100, 110, 120, ...
    """
    try:
        lines = sys.stdin.read().splitlines()

        if not lines:
            sys.exit(0)

        if mode == 'add':
            result = []
            num = start
            for line in lines:
                numbered = (num_format % num) + line
                result.append(numbered)
                num += step

        else:  # remove
            result = []
            # Pattern to match common line number formats
            # Matches: "123. ", "123: ", "123 ", "123) ", "[123] "
            pattern = r'^\s*\d+[\.\:\)\]\s]\s*'
            for line in lines:
                stripped = re.sub(pattern, '', line, count=1)
                result.append(stripped)

        # Output
        output = '\n'.join(result)
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
