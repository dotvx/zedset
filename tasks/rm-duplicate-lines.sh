#!/bin/bash
# Wrapper to safely pipe ZED_SELECTED_TEXT to rm-duplicate-lines.py and auto-paste via Hammerspoon

# Default to --first, but allow --last as optional argument
MODE="${1:---first}"

printf '%s' "$ZED_SELECTED_TEXT" | "$ZED/tasks/rm-duplicate-lines.py" "$MODE" | curl -X POST -d @- http://localhost:8888/paste -s
