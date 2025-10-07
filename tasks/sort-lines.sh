#!/bin/bash
# Wrapper to pipe ZED_SELECTED_TEXT to sort-lines.py and auto-paste via Hammerspoon

# Pass all args to sort-lines.py (e.g., --numeric, --reverse, -i, -u)
printf '%s' "$ZED_SELECTED_TEXT" | "$ZED/tasks/sort-lines.py" "$@" | curl -X POST -d @- http://localhost:8888/paste -s
