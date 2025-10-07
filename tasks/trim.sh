#!/bin/bash
# Wrapper to pipe ZED_SELECTED_TEXT to trim.py and auto-paste via Hammerspoon

# Pass all args to trim.py (e.g., --leading, --trailing, --normalize)
printf '%s' "$ZED_SELECTED_TEXT" | "$ZED/tasks/trim.py" "$@" | curl -X POST -d @- http://localhost:8888/paste -s
