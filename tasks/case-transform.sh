#!/bin/bash
# Wrapper to pipe ZED_SELECTED_TEXT to case-transform.py and auto-paste via Hammerspoon

# Pass all args to case-transform.py (e.g., --upper, --snake, --per-line)
printf '%s' "$ZED_SELECTED_TEXT" | "$ZED/tasks/case-transform.py" "$@" | curl -X POST -d @- http://localhost:8888/paste -s
