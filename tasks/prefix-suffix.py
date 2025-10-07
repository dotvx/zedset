#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "click>=8.0.0",
#     "rich>=13.0.0",
# ]
# ///

"""Add prefix or suffix to each line."""

import sys

import click
from rich.console import Console

console = Console()


@click.command()
@click.option('--prefix', type=str, help='Add prefix to each line')
@click.option('--suffix', type=str, help='Add suffix to each line')
@click.option('--number', is_flag=True, help='Add line numbers as prefix')
@click.option('--number-format', default='%d. ', help='Line number format (default: "%d. ")')
@click.option('--start', type=int, default=1, help='Starting line number (default: 1)')
@click.option('--bullet', type=str, help='Add bullet character (e.g., "- ", "* ", "• ")')
def main(prefix: str | None, suffix: str | None, number: bool, number_format: str, start: int, bullet: str | None):
    """Add prefix or suffix to each line from stdin.

    \b
    Examples:
      cat file.txt | prefix-suffix --prefix "// "
      # Comment out lines

      cat file.txt | prefix-suffix --number
      # Add line numbers

      cat file.txt | prefix-suffix --bullet "- "
      # Add bullet points

      cat file.txt | prefix-suffix --prefix "'" --suffix "'"
      # Wrap in single quotes
    """
    try:
        if not any([prefix, suffix, number, bullet]):
            console.print("[red]Error:[/red] Must specify --prefix, --suffix, --number, or --bullet", file=sys.stderr)
            sys.exit(2)

        lines = sys.stdin.read().splitlines()

        if not lines:
            sys.exit(0)

        result = []
        for i, line in enumerate(lines, start=start):
            new_line = line

            # Add prefix
            if number:
                new_line = (number_format % i) + new_line
            elif bullet:
                new_line = bullet + new_line
            elif prefix:
                new_line = prefix + new_line

            # Add suffix
            if suffix:
                new_line = new_line + suffix

            result.append(new_line)

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
