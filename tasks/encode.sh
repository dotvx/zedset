#!/bin/bash
# Wrapper to pipe ZED_SELECTED_TEXT to encode.py and auto-paste via Hammerspoon

# Pass all args to encode.py (e.g., --url-encode, --base64-decode)
printf '%s' "$ZED_SELECTED_TEXT" | "$ZED/tasks/encode.py" "$@" | curl -X POST -d @- http://localhost:8888/paste -s
