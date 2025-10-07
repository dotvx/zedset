#!/bin/bash
# Wrapper to pipe ZED_SELECTED_TEXT to prefix-suffix.py and auto-paste via Hammerspoon

# Pass all args to prefix-suffix.py (e.g., --prefix "// ", --suffix ";")
printf '%s' "$ZED_SELECTED_TEXT" | "$ZED/tasks/prefix-suffix.py" "$@" | curl -X POST -d @- http://localhost:8888/paste -s
