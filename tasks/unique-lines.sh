#!/bin/bash
# Wrapper to pipe ZED_SELECTED_TEXT to unique-lines.py and auto-paste via Hammerspoon

# Pass all args to unique-lines.py (e.g., -i, --sort)
printf '%s' "$ZED_SELECTED_TEXT" | "$ZED/tasks/unique-lines.py" "$@" | curl -X POST -d @- http://localhost:8888/paste -s
