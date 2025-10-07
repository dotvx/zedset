#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "click>=8.0.0",
#     "rich>=13.0.0",
# ]
# ///

"""Sort lines with various sorting modes."""

import sys

import click
from rich.console import Console

console = Console()


@click.command()
@click.option('--alpha', 'sort_mode', flag_value='alpha', default=True, help='Sort alphabetically (default)')
@click.option('--numeric', 'sort_mode', flag_value='numeric', help='Sort numerically')
@click.option('--length', 'sort_mode', flag_value='length', help='Sort by line length')
@click.option('--reverse', is_flag=True, help='Reverse sort order')
@click.option('--ignore-case', '-i', is_flag=True, help='Case-insensitive sort')
@click.option('--unique', '-u', is_flag=True, help='Remove duplicates after sorting')
def main(sort_mode: str, reverse: bool, ignore_case: bool, unique: bool):
    """Sort lines from stdin with various options.

    \b
    Examples:
      cat file.txt | sort-lines
      # Alphabetical sort

      cat numbers.txt | sort-lines --numeric
      # Numeric sort

      cat file.txt | sort-lines --length --reverse
      # Sort by length, longest first

      cat file.txt | sort-lines -i -u
      # Case-insensitive, deduplicated sort
    """
    try:
        lines = sys.stdin.read().splitlines()

        if not lines:
            sys.exit(0)

        # Determine sort key
        if sort_mode == 'numeric':
            # Extract first number from each line for sorting
            def numeric_key(line):
                import re
                match = re.search(r'-?\d+\.?\d*', line)
                return float(match.group()) if match else 0
            key_func = numeric_key
        elif sort_mode == 'length':
            key_func = len
        else:  # alpha
            key_func = str.lower if ignore_case else None

        # Sort
        sorted_lines = sorted(lines, key=key_func, reverse=reverse)

        # Deduplicate if requested
        if unique:
            seen = set()
            result = []
            for line in sorted_lines:
                key = line.lower() if ignore_case else line
                if key not in seen:
                    seen.add(key)
                    result.append(line)
            sorted_lines = result

        # Output
        output = '\n'.join(sorted_lines)
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
