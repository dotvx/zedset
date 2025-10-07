#!/bin/bash
# Wrapper to pipe ZED_SELECTED_TEXT to wrap-text.py and auto-paste via Hammerspoon

# Pass all args to wrap-text.py (e.g., --width 80, --preserve-short)
printf '%s' "$ZED_SELECTED_TEXT" | "$ZED/tasks/wrap-text.py" "$@" | curl -X POST -d @- http://localhost:8888/paste -s
