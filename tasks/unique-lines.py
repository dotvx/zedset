#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "click>=8.0.0",
#     "rich>=13.0.0",
# ]
# ///

"""Keep only unique lines (simple deduplication, no order preservation)."""

import sys

import click
from rich.console import Console

console = Console()


@click.command()
@click.option('--ignore-case', '-i', is_flag=True, help='Case-insensitive comparison')
@click.option('--sort', '-s', is_flag=True, help='Sort output alphabetically')
def main(ignore_case: bool, sort: bool):
    """Keep only unique lines from stdin.

    This is simpler than rm-duplicate-lines - it just deduplicates
    without caring about order preservation.

    \b
    Examples:
      cat file.txt | unique-lines
      # Remove duplicates

      cat file.txt | unique-lines -i
      # Case-insensitive deduplication

      cat file.txt | unique-lines --sort
      # Deduplicate and sort
    """
    try:
        lines = sys.stdin.read().splitlines()

        if not lines:
            sys.exit(0)

        # Use set for deduplication
        if ignore_case:
            seen = {}
            for line in lines:
                lower = line.lower()
                if lower not in seen:
                    seen[lower] = line
            result = list(seen.values())
        else:
            result = list(set(lines))

        # Sort if requested
        if sort:
            result.sort(key=str.lower if ignore_case else None)

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
