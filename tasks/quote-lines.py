#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "click>=8.0.0",
#     "rich>=13.0.0",
# ]
# ///

"""Wrap lines in quotes or brackets."""

import sys

import click
from rich.console import Console

console = Console()


def escape_quotes(text: str, quote_char: str) -> str:
    """Escape quote characters in text."""
    if quote_char == '"':
        return text.replace('\\', '\\\\').replace('"', '\\"')
    elif quote_char == "'":
        return text.replace('\\', '\\\\').replace("'", "\\'")
    elif quote_char == "`":
        return text.replace('\\', '\\\\').replace("`", "\\`")
    return text


@click.command()
@click.option('--single', 'wrap_style', flag_value='single', help="Single quotes (')")
@click.option('--double', 'wrap_style', flag_value='double', default=True, help='Double quotes (") [default]')
@click.option('--backtick', 'wrap_style', flag_value='backtick', help='Backticks (`)')
@click.option('--bracket', 'wrap_style', flag_value='bracket', help='Square brackets ([...])')
@click.option('--paren', 'wrap_style', flag_value='paren', help='Parentheses ((...)')
@click.option('--angle', 'wrap_style', flag_value='angle', help='Angle brackets (<...>)')
@click.option('--escape', is_flag=True, help='Escape quotes inside text')
@click.option('--join', type=str, help='Join lines with delimiter (e.g., ", " for arrays)')
def main(wrap_style: str, escape: bool, join: str | None):
    """Wrap each line in quotes or brackets.

    \b
    Examples:
      cat urls.txt | quote-lines
      # Wrap in double quotes

      cat names.txt | quote-lines --single --join ", "
      # Create JavaScript array: 'name1', 'name2', ...

      cat items.txt | quote-lines --bracket
      # Wrap in [brackets]

      cat sql.txt | quote-lines --single --escape
      # SQL-safe single quotes
    """
    try:
        lines = sys.stdin.read().splitlines()

        if not lines:
            sys.exit(0)

        # Define wrapping characters
        wrappers = {
            'single': ("'", "'"),
            'double': ('"', '"'),
            'backtick': ('`', '`'),
            'bracket': ('[', ']'),
            'paren': ('(', ')'),
            'angle': ('<', '>'),
        }

        left, right = wrappers[wrap_style]

        result = []
        for line in lines:
            # Escape if needed and using quotes
            if escape and wrap_style in ('single', 'double', 'backtick'):
                line = escape_quotes(line, left)

            wrapped = f"{left}{line}{right}"
            result.append(wrapped)

        # Join or output separately
        if join:
            output = join.join(result) + '\n'
        else:
            output = '\n'.join(result) + '\n'

        sys.stdout.write(output)

    except KeyboardInterrupt:
        console.print("[yellow]Cancelled[/yellow]", file=sys.stderr)
        sys.exit(130)
    except Exception as e:
        console.print(f"[red]Error:[/red] {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
