#!/bin/bash
# Encode/decode text in various formats

MODE=""

# Parse mode argument
for arg in "$@"; do
    case "$arg" in
        --url-encode) MODE="url_encode" ;;
        --url-decode) MODE="url_decode" ;;
        --base64-encode) MODE="base64_encode" ;;
        --base64-decode) MODE="base64_decode" ;;
        --html-encode) MODE="html_encode" ;;
        --html-decode) MODE="html_decode" ;;
    esac
done

if [ -z "$MODE" ]; then
    echo "Error: Must specify encoding mode" >&2
    exit 2
fi

# Perform encoding/decoding and pipe directly
case "$MODE" in
    url_encode)
        printf '%s' "$ZED_SELECTED_TEXT" | jq -sRr '@uri' | curl -X POST -d @- http://localhost:8888/paste -s
        ;;
    url_decode)
        printf '%s' "$ZED_SELECTED_TEXT" | python3 -c 'import sys, urllib.parse; print(urllib.parse.unquote(sys.stdin.read()), end="")' | curl -X POST -d @- http://localhost:8888/paste -s
        ;;
    base64_encode)
        printf '%s' "$ZED_SELECTED_TEXT" | base64 | curl -X POST -d @- http://localhost:8888/paste -s
        ;;
    base64_decode)
        printf '%s' "$ZED_SELECTED_TEXT" | base64 -d | curl -X POST -d @- http://localhost:8888/paste -s
        ;;
    html_encode)
        printf '%s' "$ZED_SELECTED_TEXT" | python3 -c 'import sys, html; print(html.escape(sys.stdin.read()), end="")' | curl -X POST -d @- http://localhost:8888/paste -s
        ;;
    html_decode)
        printf '%s' "$ZED_SELECTED_TEXT" | python3 -c 'import sys, html; print(html.unescape(sys.stdin.read()), end="")' | curl -X POST -d @- http://localhost:8888/paste -s
        ;;
esac
