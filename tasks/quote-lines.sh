#!/bin/bash
# Wrapper to pipe ZED_SELECTED_TEXT to quote-lines.py and auto-paste via Hammerspoon

# Pass all args to quote-lines.py (e.g., --single, --double, --escape)
printf '%s' "$ZED_SELECTED_TEXT" | "$ZED/tasks/quote-lines.py" "$@" | curl -X POST -d @- http://localhost:8888/paste -s
