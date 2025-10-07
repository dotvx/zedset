#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "click>=8.0.0",
#     "rich>=13.0.0",
# ]
# ///

"""Manipulate indentation: convert tabs/spaces, indent/dedent lines."""

import re
import sys

import click
from rich.console import Console

console = Console()


def detect_indent_style(lines: list[str]) -> tuple[str, int]:
    """Detect indentation style (tabs or spaces) and width.

    Returns: (style, width) where style is 'tabs' or 'spaces'
    """
    tab_lines = 0
    space_lines = 0
    space_widths = []

    for line in lines:
        if not line or line[0] not in (" ", "\t"):
            continue

        if line[0] == "\t":
            tab_lines += 1
        elif line[0] == " ":
            space_lines += 1
            # Count leading spaces
            spaces = len(line) - len(line.lstrip(" "))
            space_widths.append(spaces)

    # Determine style by majority
    style = "tabs" if tab_lines > space_lines else "spaces"

    # Calculate common space width (mode)
    if space_widths:
        width = max(set(space_widths), key=space_widths.count)
    else:
        width = 4  # Default

    return style, width


def get_indent_level(line: str, indent_char: str, indent_width: int) -> int:
    """Get indentation level of a line."""
    if indent_char == "\t":
        return len(line) - len(line.lstrip("\t"))
    else:
        spaces = len(line) - len(line.lstrip(" "))
        return spaces // indent_width


def apply_indent_level(
    line: str, level: int, indent_char: str, indent_width: int
) -> str:
    """Apply indentation level to a line (removing old indent)."""
    stripped = line.lstrip()
    if indent_char == "\t":
        return "\t" * level + stripped
    else:
        return " " * (level * indent_width) + stripped


@click.command()
@click.option(
    "--spaces", type=int, metavar="N", help="Convert indentation to N spaces per level"
)
@click.option("--tabs", is_flag=True, help="Convert indentation to tabs")
@click.option("--indent", type=int, metavar="N", help="Increase indentation by N levels")
@click.option("--dedent", type=int, metavar="N", help="Decrease indentation by N levels")
def main(spaces: int | None, tabs: bool, indent: int | None, dedent: int | None):
    """Manipulate indentation of text from stdin.

    Can convert between tabs/spaces or shift indentation levels.

    \b
    Examples:
      # Convert tabs to 4 spaces
      cat file.py | indent --spaces 4

      # Convert spaces to tabs
      cat file.py | indent --tabs

      # Increase indentation by 1 level
      cat file.py | indent --indent 1

      # Decrease indentation by 2 levels
      cat file.py | indent --dedent 2

      # Convert to 2 spaces and increase by 1 level
      cat file.py | indent --spaces 2 --indent 1
    """
    try:
        lines = sys.stdin.read().splitlines()

        if not lines:
            sys.exit(0)

        # Detect current indentation style
        current_style, current_width = detect_indent_style(lines)

        # Determine target style
        if tabs:
            target_char = "\t"
            target_width = 1
        elif spaces is not None:
            target_char = " "
            target_width = spaces
        else:
            # Keep current style
            target_char = "\t" if current_style == "tabs" else " "
            target_width = current_width

        # Process each line
        result = []
        for line in lines:
            if not line.strip():  # Empty or whitespace-only
                result.append("")
                continue

            # Get current indent level
            level = get_indent_level(
                line, "\t" if current_style == "tabs" else " ", current_width
            )

            # Apply indent/dedent shift
            if indent:
                level += indent
            if dedent:
                level = max(0, level - dedent)

            # Apply new indentation
            new_line = apply_indent_level(line, level, target_char, target_width)
            result.append(new_line)

        # Output
        output = "\n".join(result)
        if lines:
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
