#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "click>=8.0.0",
#     "rich>=13.0.0",
# ]
# ///

"""Sort JSON/JSONC keys alphabetically."""

import json
import re
import sys

import click
from rich.console import Console

console = Console()


def strip_json_comments(text: str) -> str:
    """Remove // and /* */ style comments from JSONC text."""
    # Remove /* */ block comments
    text = re.sub(r"/\*.*?\*/", "", text, flags=re.DOTALL)
    # Remove // line comments (but not in strings)
    lines = []
    for line in text.splitlines():
        in_string = False
        escaped = False
        result = []
        i = 0
        while i < len(line):
            char = line[i]

            if escaped:
                result.append(char)
                escaped = False
                i += 1
                continue

            if char == "\\":
                escaped = True
                result.append(char)
                i += 1
                continue

            if char == '"':
                in_string = not in_string
                result.append(char)
                i += 1
                continue

            if not in_string and i < len(line) - 1 and line[i : i + 2] == "//":
                break

            result.append(char)
            i += 1

        lines.append("".join(result))

    return "\n".join(lines)


def sort_dict_recursive(obj):
    """Recursively sort all dictionary keys in nested structure."""
    if isinstance(obj, dict):
        return {k: sort_dict_recursive(v) for k, v in sorted(obj.items())}
    elif isinstance(obj, list):
        return [sort_dict_recursive(item) for item in obj]
    else:
        return obj


@click.command()
@click.option(
    "--indent", type=int, default=2, help="Indentation spaces (default: 2)"
)
@click.option(
    "--compact", is_flag=True, help="Compact output (no extra whitespace)"
)
def main(indent: int, compact: bool):
    """Sort JSON/JSONC keys alphabetically from stdin.

    Strips comments from JSONC input and outputs clean sorted JSON.

    \b
    Examples:
      # Sort JSON keys with 2-space indent
      cat config.json | sort-json

      # Sort with 4-space indent
      cat config.json | sort-json --indent 4

      # Compact output
      cat config.json | sort-json --compact
    """
    try:
        input_text = sys.stdin.read()

        if not input_text.strip():
            console.print("[yellow]Warning:[/yellow] Empty input", file=sys.stderr)
            sys.exit(0)

        # Strip comments for JSONC support
        cleaned = strip_json_comments(input_text)

        try:
            data = json.loads(cleaned)
        except json.JSONDecodeError as e:
            console.print(f"[red]JSON parse error:[/red] {e}", file=sys.stderr)
            sys.exit(1)

        # Sort keys recursively
        sorted_data = sort_dict_recursive(data)

        # Output
        if compact:
            output = json.dumps(sorted_data, separators=(",", ":"), ensure_ascii=False)
        else:
            output = json.dumps(sorted_data, indent=indent, ensure_ascii=False)

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
