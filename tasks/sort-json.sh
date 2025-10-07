#!/bin/bash
# Wrapper to pipe ZED_SELECTED_TEXT to sort-json.py and auto-paste via Hammerspoon

# Pass all args to sort-json.py (e.g., --indent 4, --compact)
printf '%s' "$ZED_SELECTED_TEXT" | "$ZED/tasks/sort-json.py" "$@" | curl -X POST -d @- http://localhost:8888/paste -s
