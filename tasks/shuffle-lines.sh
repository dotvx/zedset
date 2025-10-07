#!/bin/bash
# Wrapper to pipe ZED_SELECTED_TEXT to shuffle-lines.py and auto-paste via Hammerspoon

# Pass all args to shuffle-lines.py (e.g., --seed 42)
printf '%s' "$ZED_SELECTED_TEXT" | "$ZED/tasks/shuffle-lines.py" "$@" | curl -X POST -d @- http://localhost:8888/paste -s
