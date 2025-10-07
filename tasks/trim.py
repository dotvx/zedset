#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "click>=8.0.0",
#     "rich>=13.0.0",
# ]
# ///

"""Trim and normalize whitespace in text."""

import re
import sys

import click
from rich.console import Console

console = Console()


@click.command()
@click.option('--leading', is_flag=True, help='Trim leading whitespace only')
@click.option('--trailing', is_flag=True, help='Trim trailing whitespace only')
@click.option('--both', is_flag=True, help='Trim both sides (default if no option specified)')
@click.option('--normalize', is_flag=True, help='Collapse internal whitespace to single space')
@click.option('--blank-lines', is_flag=True, help='Remove blank lines')
def main(leading: bool, trailing: bool, both: bool, normalize: bool, blank_lines: bool):
    """Trim and normalize whitespace from stdin.

    By default, trims both leading and trailing whitespace.

    \b
    Examples:
      cat file.txt | trim
      # Trim both sides

      cat file.txt | trim --leading
      # Trim left only

      cat file.txt | trim --normalize
      # Collapse multiple spaces to one

      cat file.txt | trim --blank-lines
      # Remove empty lines
    """
    try:
        lines = sys.stdin.read().splitlines()

        if not lines:
            sys.exit(0)

        # Default to both if no specific side specified
        if not (leading or trailing) and not normalize and not blank_lines:
            both = True

        result = []
        for line in lines:
            # Skip blank lines if requested
            if blank_lines and not line.strip():
                continue

            # Normalize internal whitespace
            if normalize:
                line = re.sub(r'\s+', ' ', line)

            # Trim sides
            if both or (leading and trailing):
                line = line.strip()
            elif leading:
                line = line.lstrip()
            elif trailing:
                line = line.rstrip()

            result.append(line)

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
