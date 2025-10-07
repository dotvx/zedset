#!/bin/bash
# Wrapper to pipe ZED_SELECTED_TEXT to indent.py and auto-paste via Hammerspoon

# Pass all args to indent.py (e.g., --spaces 4, --tabs, --indent 1)
printf '%s' "$ZED_SELECTED_TEXT" | "$ZED/tasks/indent.py" "$@" | curl -X POST -d @- http://localhost:8888/paste -s
