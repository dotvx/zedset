#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "click>=8.0.0",
#     "rich>=13.0.0",
# ]
# ///

"""Encode and decode text in various formats."""

import base64
import html
import sys
import urllib.parse

import click
from rich.console import Console

console = Console()


@click.command()
@click.option('--url-encode', 'mode', flag_value='url_encode', help='URL encode (percent encoding)')
@click.option('--url-decode', 'mode', flag_value='url_decode', help='URL decode')
@click.option('--uri-component', 'mode', flag_value='uri_component', help='encodeURIComponent style')
@click.option('--base64-encode', 'mode', flag_value='base64_encode', help='Base64 encode')
@click.option('--base64-decode', 'mode', flag_value='base64_decode', help='Base64 decode')
@click.option('--html-encode', 'mode', flag_value='html_encode', help='HTML entity encode')
@click.option('--html-decode', 'mode', flag_value='html_decode', help='HTML entity decode')
def main(mode: str | None):
    """Encode or decode text from stdin.

    \b
    Examples:
      echo "hello world" | encode --url-encode
      # Output: hello%20world

      echo "aGVsbG8=" | encode --base64-decode
      # Output: hello

      echo "a < b && c > d" | encode --html-encode
      # Output: a &lt; b &amp;&amp; c &gt; d
    """
    try:
        if not mode:
            console.print("[red]Error:[/red] Must specify an encoding mode", file=sys.stderr)
            sys.exit(2)

        input_text = sys.stdin.read()

        if not input_text:
            sys.exit(0)

        # Strip trailing newline for processing
        text = input_text.rstrip('\n')

        # Perform encoding/decoding
        if mode == 'url_encode':
            output = urllib.parse.quote(text)
        elif mode == 'url_decode':
            output = urllib.parse.unquote(text)
        elif mode == 'uri_component':
            # encodeURIComponent style (more aggressive than quote)
            output = urllib.parse.quote(text, safe='')
        elif mode == 'base64_encode':
            encoded_bytes = base64.b64encode(text.encode('utf-8'))
            output = encoded_bytes.decode('ascii')
        elif mode == 'base64_decode':
            try:
                decoded_bytes = base64.b64decode(text)
                output = decoded_bytes.decode('utf-8')
            except Exception as e:
                console.print(f"[red]Base64 decode error:[/red] {e}", file=sys.stderr)
                sys.exit(1)
        elif mode == 'html_encode':
            output = html.escape(text)
        elif mode == 'html_decode':
            output = html.unescape(text)

        # Preserve original trailing newline
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
