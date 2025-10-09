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

# Perform encoding/decoding
case "$MODE" in
    url_encode)
        output=$(printf '%s' "$ZED_SELECTED_TEXT" | jq -sRr '@uri')
        ;;
    url_decode)
        output=$(printf '%s' "$ZED_SELECTED_TEXT" | python3 -c 'import sys, urllib.parse; print(urllib.parse.unquote(sys.stdin.read()), end="")')
        ;;
    base64_encode)
        output=$(printf '%s' "$ZED_SELECTED_TEXT" | base64)
        ;;
    base64_decode)
        output=$(printf '%s' "$ZED_SELECTED_TEXT" | base64 -d)
        ;;
    html_encode)
        output=$(printf '%s' "$ZED_SELECTED_TEXT" | python3 -c 'import sys, html; print(html.escape(sys.stdin.read()), end="")')
        ;;
    html_decode)
        output=$(printf '%s' "$ZED_SELECTED_TEXT" | python3 -c 'import sys, html; print(html.unescape(sys.stdin.read()), end="")')
        ;;
esac

# Send to Hammerspoon
printf '%s' "$output" | curl -X POST -d @- http://localhost:8888/paste -s
