#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "click>=8.0.0",
#     "rich>=13.0.0",
# ]
# ///

"""Transform text between different case styles."""

import re
import sys

import click
from rich.console import Console

console = Console()


def to_camel_case(text: str) -> str:
    """Convert to camelCase."""
    # Split on non-alphanumeric chars and underscores
    words = re.split(r'[^a-zA-Z0-9]+', text)
    words = [w for w in words if w]  # Remove empty strings
    if not words:
        return text
    return words[0].lower() + ''.join(w.capitalize() for w in words[1:])


def to_pascal_case(text: str) -> str:
    """Convert to PascalCase."""
    words = re.split(r'[^a-zA-Z0-9]+', text)
    words = [w for w in words if w]
    if not words:
        return text
    return ''.join(w.capitalize() for w in words)


def to_snake_case(text: str) -> str:
    """Convert to snake_case."""
    # Handle PascalCase/camelCase
    text = re.sub(r'([A-Z]+)([A-Z][a-z])', r'\1_\2', text)
    text = re.sub(r'([a-z\d])([A-Z])', r'\1_\2', text)
    # Replace non-alphanumeric with underscore
    text = re.sub(r'[^a-zA-Z0-9]+', '_', text)
    return text.lower().strip('_')


def to_kebab_case(text: str) -> str:
    """Convert to kebab-case."""
    # Same as snake_case but with hyphens
    text = re.sub(r'([A-Z]+)([A-Z][a-z])', r'\1-\2', text)
    text = re.sub(r'([a-z\d])([A-Z])', r'\1-\2', text)
    text = re.sub(r'[^a-zA-Z0-9]+', '-', text)
    return text.lower().strip('-')


def to_screaming_snake_case(text: str) -> str:
    """Convert to SCREAMING_SNAKE_CASE."""
    return to_snake_case(text).upper()


def to_dot_case(text: str) -> str:
    """Convert to dot.case."""
    text = re.sub(r'([A-Z]+)([A-Z][a-z])', r'\1.\2', text)
    text = re.sub(r'([a-z\d])([A-Z])', r'\1.\2', text)
    text = re.sub(r'[^a-zA-Z0-9]+', '.', text)
    return text.lower().strip('.')


@click.command()
@click.option('--upper', 'case_style', flag_value='upper', help='UPPERCASE')
@click.option('--lower', 'case_style', flag_value='lower', help='lowercase')
@click.option('--title', 'case_style', flag_value='title', help='Title Case')
@click.option('--camel', 'case_style', flag_value='camel', help='camelCase')
@click.option('--pascal', 'case_style', flag_value='pascal', help='PascalCase')
@click.option('--snake', 'case_style', flag_value='snake', help='snake_case')
@click.option('--kebab', 'case_style', flag_value='kebab', help='kebab-case')
@click.option('--screaming', 'case_style', flag_value='screaming', help='SCREAMING_SNAKE_CASE')
@click.option('--dot', 'case_style', flag_value='dot', help='dot.case')
@click.option('--per-line', is_flag=True, help='Transform each line separately (default: entire text)')
def main(case_style: str | None, per_line: bool):
    """Transform text between different case styles.

    By default, transforms the entire input as one string.
    Use --per-line to transform each line individually.

    \b
    Examples:
      echo "hello world" | case-transform --upper
      # Output: HELLO WORLD

      echo "HelloWorld" | case-transform --snake
      # Output: hello_world

      echo -e "foo bar\\nbaz qux" | case-transform --camel --per-line
      # Output: fooBar\\nbazQux
    """
    try:
        if not case_style:
            console.print("[red]Error:[/red] Must specify a case style", file=sys.stderr)
            sys.exit(2)

        input_text = sys.stdin.read()
        if not input_text:
            sys.exit(0)

        # Transform function mapping
        transforms = {
            'upper': str.upper,
            'lower': str.lower,
            'title': str.title,
            'camel': to_camel_case,
            'pascal': to_pascal_case,
            'snake': to_snake_case,
            'kebab': to_kebab_case,
            'screaming': to_screaming_snake_case,
            'dot': to_dot_case,
        }

        transform_func = transforms[case_style]

        if per_line:
            lines = input_text.splitlines()
            result = [transform_func(line) for line in lines]
            output = '\n'.join(result)
            if lines:
                output += '\n'
        else:
            # Strip trailing newline for whole-text transform
            text = input_text.rstrip('\n')
            output = transform_func(text)
            if input_text.endswith('\n'):
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
