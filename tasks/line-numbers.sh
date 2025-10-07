#!/bin/bash
# Wrapper to pipe ZED_SELECTED_TEXT to line-numbers.py and auto-paste via Hammerspoon

# Pass all args to line-numbers.py (e.g., --add, --remove, --format "%03d: ")
printf '%s' "$ZED_SELECTED_TEXT" | "$ZED/tasks/line-numbers.py" "$@" | curl -X POST -d @- http://localhost:8888/paste -s
