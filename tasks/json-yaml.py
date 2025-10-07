#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "click>=8.0.0",
#     "rich>=13.0.0",
#     "pyyaml>=6.0",
# ]
# ///

"""Bidirectional JSON ↔ YAML converter with JSONC support."""

import json
import re
import sys

import click
import yaml
from rich.console import Console

console = Console()


def strip_json_comments(text: str) -> str:
    """Remove // and /* */ style comments from JSONC text."""
    # Remove /* */ block comments
    text = re.sub(r"/\*.*?\*/", "", text, flags=re.DOTALL)
    # Remove // line comments (but not in strings)
    lines = []
    for line in text.splitlines():
        # Simple heuristic: remove // comments not inside quotes
        # This is not perfect but works for most cases
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
                # Comment starts here, ignore rest of line
                break

            result.append(char)
            i += 1

        lines.append("".join(result))

    return "\n".join(lines)


def detect_format(text: str) -> str:
    """Auto-detect if input is JSON/JSONC or YAML."""
    text_stripped = text.strip()

    # Check for JSON-like structure
    if text_stripped.startswith("{") or text_stripped.startswith("["):
        return "json"

    # Check for YAML-like structure (key: value, arrays with -, etc.)
    if re.search(r"^\w+\s*:", text_stripped, re.MULTILINE):
        return "yaml"

    # Default to YAML for ambiguous cases
    return "yaml"


@click.command()
@click.option(
    "--to-json",
    "target_format",
    flag_value="json",
    help="Convert to JSON (auto-detects input)",
)
@click.option(
    "--to-yaml",
    "target_format",
    flag_value="yaml",
    help="Convert to YAML (auto-detects input)",
)
@click.option(
    "--indent",
    type=int,
    default=2,
    help="Indentation spaces for JSON output (default: 2)",
)
def main(target_format: str | None, indent: int):
    """Bidirectional JSON ↔ YAML converter with JSONC support.

    Auto-detects input format and converts to specified format.
    Strips comments from JSONC input.

    \b
    Examples:
      # Convert JSON to YAML
      cat config.json | json-yaml --to-yaml

      # Convert YAML to JSON
      cat config.yaml | json-yaml --to-json

      # JSONC to YAML (strips comments)
      cat config.jsonc | json-yaml --to-yaml
    """
    try:
        input_text = sys.stdin.read()

        if not input_text.strip():
            console.print("[yellow]Warning:[/yellow] Empty input", file=sys.stderr)
            sys.exit(0)

        # Detect input format
        input_format = detect_format(input_text)

        # Auto-detect target if not specified
        if not target_format:
            target_format = "yaml" if input_format == "json" else "json"

        # Parse input
        if input_format == "json":
            # Strip comments for JSONC support
            cleaned = strip_json_comments(input_text)
            try:
                data = json.loads(cleaned)
            except json.JSONDecodeError as e:
                console.print(f"[red]JSON parse error:[/red] {e}", file=sys.stderr)
                sys.exit(1)
        else:  # YAML
            try:
                data = yaml.safe_load(input_text)
            except yaml.YAMLError as e:
                console.print(f"[red]YAML parse error:[/red] {e}", file=sys.stderr)
                sys.exit(1)

        # Convert to target format
        if target_format == "json":
            output = json.dumps(data, indent=indent, ensure_ascii=False)
            output += "\n"
        else:  # YAML
            output = yaml.dump(
                data,
                default_flow_style=False,
                allow_unicode=True,
                sort_keys=False,
                indent=indent,
            )

        sys.stdout.write(output)

    except KeyboardInterrupt:
        console.print("[yellow]Cancelled[/yellow]", file=sys.stderr)
        sys.exit(130)
    except Exception as e:
        console.print(f"[red]Error:[/red] {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
