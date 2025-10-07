#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "click>=8.0.0",
#     "rich>=13.0.0",
# ]
# ///

"""Remove duplicate lines from text, keeping first or last occurrence."""

import sys

import click
from rich.console import Console

console = Console()


@click.command()
@click.option(
    "--first",
    "keep_mode",
    flag_value="first",
    default=True,
    help="Keep first occurrence of duplicates (default)",
)
@click.option(
    "--last",
    "keep_mode",
    flag_value="last",
    help="Keep last occurrence of duplicates",
)
def main(keep_mode: str):
    """Remove duplicate lines from stdin, preserving order.

    By default, keeps the FIRST occurrence of each unique line.
    Use --last to keep the LAST occurrence instead.

    \b
    Examples:
      echo -e "a\\nb\\na\\nc" | rm-duplicate-lines
      # Output: a, b, c (first 'a' kept)

      echo -e "a\\nb\\na\\nc" | rm-duplicate-lines --last
      # Output: b, a, c (last 'a' kept)
    """
    try:
        lines = sys.stdin.read().splitlines()

        if keep_mode == "first":
            # Keep first occurrence: track seen lines, output immediately
            seen = set()
            result = []
            for line in lines:
                if line not in seen:
                    seen.add(line)
                    result.append(line)

        else:  # keep_mode == "last"
            # Keep last occurrence: reverse, dedupe, reverse back
            seen = set()
            result = []
            for line in reversed(lines):
                if line not in seen:
                    seen.add(line)
                    result.append(line)
            result.reverse()

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
