#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "click>=8.0.0",
#     "rich>=13.0.0",
# ]
# ///

"""Hard-wrap long lines to specified width."""

import sys
import textwrap

import click
from rich.console import Console

console = Console()


@click.command()
@click.option('--width', '-w', type=int, default=80, help='Wrap width in characters (default: 80)')
@click.option('--preserve-short', is_flag=True, help="Don't wrap lines shorter than width")
@click.option('--break-words', is_flag=True, help='Break mid-word if necessary')
@click.option('--indent', type=str, default='', help='Indent wrapped lines with this prefix')
def main(width: int, preserve_short: bool, break_words: bool, indent: str):
    """Hard-wrap long lines to specified width.

    \b
    Examples:
      cat long-line.txt | wrap-text --width 60
      # Wrap at 60 characters

      cat text.txt | wrap-text --preserve-short
      # Only wrap lines exceeding width

      cat text.txt | wrap-text --indent "  "
      # Indent continuation lines
    """
    try:
        if width <= 0:
            console.print("[red]Error:[/red] Width must be positive", file=sys.stderr)
            sys.exit(2)

        lines = sys.stdin.read().splitlines()

        if not lines:
            sys.exit(0)

        result = []
        for line in lines:
            # Skip short lines if preserve-short
            if preserve_short and len(line) <= width:
                result.append(line)
                continue

            # Wrap the line
            wrapped = textwrap.fill(
                line,
                width=width,
                subsequent_indent=indent,
                break_long_words=break_words,
                break_on_hyphens=True,
            )
            result.append(wrapped)

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
